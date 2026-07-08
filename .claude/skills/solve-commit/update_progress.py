#!/usr/bin/env python3
"""Recompute the progress table from the checkboxes that are the source of truth.

Counts `- [x]` lines under each problem section of README.md, then rewrites that
README's summary table and its `**N problems solved**` line in place.

The table is solved-only: no denominators, no percentages. The CSES problem set
is far larger than the sections listed here, so there's no fixed finish line
worth tracking against.

Only the sections listed in SECTIONS count. README.md also carries an Interview
Topic Checklist, String Algorithms, and a Weekly Schedule whose checkboxes are
not solved problems; leaving them out is the whole point of having an explicit
allowlist here rather than counting every box in the file.

Idempotent: safe to run any time, not just after solving. Run from anywhere.

    python3 .claude/skills/solve-commit/update_progress.py [--check]

--check exits 1 if the file would change, printing a diff. Nothing is written.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
README = REPO / "README.md"

# (summary-table label, "## section heading")
# The label and the heading differ in places ("Introductory" vs "Introductory
# Problems"), so both are spelled out rather than derived from one another.
SECTIONS: list[tuple[str, str]] = [
    ("Introductory", "Introductory Problems"),
    ("Sorting and Searching", "Sorting and Searching"),
    ("Dynamic Programming", "Dynamic Programming Problems"),
    ("Graph Algorithms", "Graph Algorithms Problems"),
    ("Tree Algorithms", "Tree Algorithms"),
    ("Range Queries", "Range Queries"),
]

DONE = re.compile(r"^- \[x\] ", re.I)
TODO = re.compile(r"^- \[ \] ")
HEADING = re.compile(r"^## +(.*?)\s*$")


def count_sections(text: str) -> dict[str, int]:
    """Return {heading: done} for the requested headings."""
    tally: dict[str, int] = {h: 0 for _, h in SECTIONS}
    seen: set[str] = set()
    current: str | None = None
    for line in text.splitlines():
        if m := HEADING.match(line):
            current = m.group(1)
        elif current in tally:
            if DONE.match(line):
                tally[current] += 1
                seen.add(current)
            elif TODO.match(line):
                seen.add(current)

    missing = [h for _, h in SECTIONS if h not in seen]
    if missing:
        raise SystemExit(
            "error: README.md has no checkboxes under: "
            + ", ".join(missing)
            + "\n  A heading was renamed, or its list is empty. "
            "Fix the heading or update SECTIONS in this script."
        )
    return tally


def replace_row(text: str, label: str, cells: str) -> str:
    """Rewrite the table row whose first cell is `label`. Must be unique."""
    pattern = re.compile(r"^\|\s*" + re.escape(label) + r"\s*\|[^\n]*$", re.M)
    new = f"| {label} | {cells} |"
    text, n = pattern.subn(lambda _: new, text)
    if n != 1:
        raise SystemExit(f"error: expected exactly 1 table row for {label!r}, found {n}")
    return text


def render(text: str) -> str:
    """Compute the new content of the README. Pure; no writes."""
    counts = count_sections(text)
    done = sum(counts.values())

    for label, heading in SECTIONS:
        text = replace_row(text, label, str(counts[heading]))
    text = replace_row(text, "**Total**", f"**{done}**")

    # The prose line above the table, e.g. "**58 problems solved**".
    return re.sub(
        r"^\*\*\d+ problems? solved\*\*",
        f"**{done} problem{'s' if done != 1 else ''} solved**",
        text,
        count=1,
        flags=re.M,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if anything would change")
    args = ap.parse_args()

    if not README.exists():
        raise SystemExit("error: README.md not found")

    before = README.read_text()
    after = render(before)

    if before == after:
        print("progress table already up to date")
        return 0

    if args.check:
        sys.stdout.writelines(
            difflib.unified_diff(
                before.splitlines(True),
                after.splitlines(True),
                fromfile="README.md",
                tofile="README.md (recomputed)",
            )
        )
        print("\nREADME.md is out of date", file=sys.stderr)
        return 1

    README.write_text(after)
    print("updated README.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
