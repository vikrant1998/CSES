#!/usr/bin/env python3
"""Recompute every progress table from the checkboxes that are the source of truth.

Counts `- [x]` / `- [ ]` lines under each track README's problem sections, then
rewrites that README's summary table and the root README's roll-up in place.

Only the sections listed in TRACKS count. CSES/README.md also carries an
Interview Topic Checklist, String Algorithms, and a Weekly Schedule whose
checkboxes are not solved problems; leaving them out is the whole point of
having an explicit allowlist here rather than counting every box in the file.

Idempotent: safe to run any time, not just after solving. Run from anywhere.

    python3 .claude/skills/solve-commit/update_progress.py [--check]

--check exits 1 if any file would change, printing a diff. Nothing is written.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]

# track -> (readme, [(summary-table label, "## section heading"), ...])
# The label and the heading differ in CSES ("Introductory" vs "Introductory
# Problems"), so both are spelled out rather than derived from one another.
TRACKS: dict[str, tuple[str, list[tuple[str, str]]]] = {
    "CSES": (
        "CSES/README.md",
        [
            ("Introductory", "Introductory Problems"),
            ("Sorting and Searching", "Sorting and Searching"),
            ("Dynamic Programming", "Dynamic Programming Problems"),
            ("Graph Algorithms", "Graph Algorithms Problems"),
            ("Tree Algorithms", "Tree Algorithms"),
            ("Range Queries", "Range Queries"),
        ],
    ),
    "NeetCode 150": (
        "NeetCode150/README.md",
        [
            ("Arrays & Hashing", "Arrays & Hashing"),
            ("Two Pointers", "Two Pointers"),
            ("Sliding Window", "Sliding Window"),
            ("Stack", "Stack"),
            ("Binary Search", "Binary Search"),
            ("Linked List", "Linked List"),
            ("Trees", "Trees"),
            ("Tries", "Tries"),
            ("Heap / Priority Queue", "Heap / Priority Queue"),
            ("Backtracking", "Backtracking"),
            ("Graphs", "Graphs"),
            ("Advanced Graphs", "Advanced Graphs"),
            ("1-D Dynamic Programming", "1-D Dynamic Programming"),
            ("2-D Dynamic Programming", "2-D Dynamic Programming"),
            ("Greedy", "Greedy"),
            ("Intervals", "Intervals"),
            ("Math & Geometry", "Math & Geometry"),
            ("Bit Manipulation", "Bit Manipulation"),
        ],
    ),
}

DONE = re.compile(r"^- \[x\] ", re.I)
TODO = re.compile(r"^- \[ \] ")
HEADING = re.compile(r"^## +(.*?)\s*$")


def count_sections(readme: Path, sections: list[tuple[str, str]]) -> dict[str, tuple[int, int]]:
    """Return {heading: (done, total)} for the requested headings."""
    tally: dict[str, list[int]] = {h: [0, 0] for _, h in sections}
    current: str | None = None
    for line in readme.read_text().splitlines():
        if m := HEADING.match(line):
            current = m.group(1)
        elif current in tally:
            if DONE.match(line):
                tally[current][0] += 1
                tally[current][1] += 1
            elif TODO.match(line):
                tally[current][1] += 1

    missing = [h for h, (_, total) in tally.items() if total == 0]
    if missing:
        raise SystemExit(
            f"error: {readme.relative_to(REPO)} has no checkboxes under: "
            + ", ".join(missing)
            + "\n  A heading was renamed, or its list is empty. "
            "Fix the heading or update TRACKS in this script."
        )
    return {h: (d, t) for h, (d, t) in tally.items()}


def replace_row(text: str, label: str, cells: str) -> str:
    """Rewrite the table row whose first cell is `label`.

    Requires the row to be unique in `text` -- the root README has one
    `**Total**` row per track table, so callers must narrow to a single
    section first (see `within_section`) rather than relying on first-match.
    """
    pattern = re.compile(
        r"^\|\s*" + re.escape(label) + r"\s*\|[^\n]*$",
        re.M,
    )
    new = f"| {label} | {cells} |"
    text, n = pattern.subn(lambda _: new, text)
    if n != 1:
        raise SystemExit(f"error: expected exactly 1 table row for {label!r}, found {n}")
    return text


def within_section(text: str, heading: str, fn) -> str:
    """Apply `fn` to just the slice of `text` under `## heading`."""
    lines = text.splitlines(keepends=True)
    start = next(
        (i for i, l in enumerate(lines) if (m := HEADING.match(l)) and m.group(1) == heading),
        None,
    )
    if start is None:
        raise SystemExit(f"error: no '## {heading}' section found")
    end = next(
        (i for i in range(start + 1, len(lines)) if HEADING.match(lines[i])),
        len(lines),
    )
    body = "".join(lines[start:end])
    return "".join(lines[:start]) + fn(body) + "".join(lines[end:])


def render(paths: dict[Path, str]) -> dict[Path, str]:
    """Compute the new content of every README. Pure; no writes."""
    out = dict(paths)
    totals: dict[str, tuple[int, int]] = {}

    for track, (rel, sections) in TRACKS.items():
        path = REPO / rel
        counts = count_sections(path, sections)
        text = out[path]

        done = sum(d for d, _ in counts.values())
        total = sum(t for _, t in counts.values())
        totals[track] = (done, total)

        has_total_col = "| Topic | Solved | Total |" in text
        for label, heading in sections:
            d, t = counts[heading]
            text = replace_row(text, label, f"{d} | {t}" if has_total_col else str(d))
        text = replace_row(
            text,
            "**Total**",
            f"**{done}** | **{total}**" if has_total_col else f"**{done}**",
        )

        # The prose line above the table, e.g. "**58 problems solved**".
        text = re.sub(
            r"^\*\*\d+ problems? solved\*\*",
            f"**{done} problem{'s' if done != 1 else ''} solved**",
            text,
            count=1,
            flags=re.M,
        )
        out[path] = text

    # Root roll-up: one row per track plus a combined row.
    root = REPO / "README.md"
    text = out[root]
    for track, (rel, _) in TRACKS.items():
        done, total = totals[track]
        link = f"[{track}]({rel})" if track != "CSES" else f"[CSES Problem Set]({rel})"
        text = replace_row(text, link, f"{done} | {total} | {pct(done, total)}")

    cd = sum(d for d, _ in totals.values())
    ct = sum(t for _, t in totals.values())
    text = replace_row(text, "**Combined**", f"**{cd}** | **{ct}** | **{pct(cd, ct)}**")

    # Root per-topic tables mirror each track's. Each lives under its own
    # `## [Track](path)` heading and has its own **Total** row, so scope the
    # rewrite to that section -- a bare replace_row would hit the wrong table.
    for track, (rel, sections) in TRACKS.items():
        counts = count_sections(REPO / rel, sections)
        done, total = totals[track]

        def rewrite(body: str, sections=sections, counts=counts, done=done, total=total) -> str:
            for label, heading in sections:
                d, t = counts[heading]
                body = replace_row(body, label, f"{d} | {t}")
            return replace_row(body, "**Total**", f"**{done}** | **{total}**")

        text = within_section(text, f"[{track}]({rel})", rewrite)

    out[root] = text
    return out


def pct(done: int, total: int) -> str:
    return f"{round(100 * done / total) if total else 0}%"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if anything would change")
    args = ap.parse_args()

    files = [REPO / "README.md"] + [REPO / rel for rel, _ in TRACKS.values()]
    for f in files:
        if not f.exists():
            raise SystemExit(f"error: {f.relative_to(REPO)} not found")

    before = {f: f.read_text() for f in files}
    after = render(before)

    changed = [f for f in files if before[f] != after[f]]
    if args.check:
        for f in changed:
            sys.stdout.writelines(
                difflib.unified_diff(
                    before[f].splitlines(True),
                    after[f].splitlines(True),
                    fromfile=str(f.relative_to(REPO)),
                    tofile=f"{f.relative_to(REPO)} (recomputed)",
                )
            )
        if changed:
            print(f"\n{len(changed)} file(s) out of date", file=sys.stderr)
            return 1
        print("all progress tables up to date")
        return 0

    for f in changed:
        f.write_text(after[f])
        print(f"updated {f.relative_to(REPO)}")
    if not changed:
        print("all progress tables already up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
