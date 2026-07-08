---
name: solve-commit
description: Finalize a solved CSES problem — check it off in the README with today's date, recompute the progress table, commit with the project's message convention, and push. Use whenever the user says a problem is solved/passing and wants it recorded, committed, or pushed (e.g. "add to git and update readme", "commit this solution", "mark X done and push").
---

# Finalize a solved problem

Solutions live at `<Topic>/<problem>/` in the repo root — `Introductory/`,
`Sorting&Searching/`, `DynamicProgramming/`, `Graph/`, `Tree/`, `RangeQueries/`.
The single `README.md` at the root is the checklist.

Do these steps in order.

## 1. Verify the solution actually runs

Do not skip this and do not infer it from the code looking correct.

- If the problem folder has a `tests/` dir, run them: `./check.sh <Topic>/<problem>/<file>.py <Topic>/<problem>/tests`
- Otherwise execute the file against a few cases yourself, including the edge
  cases — empty input, single element, duplicates at the boundary.

If it fails, fix it and re-run before going further. Never commit a solution
that has not been executed in this session.

## 2. Check it off in the README

Each problem is a checklist line under its topic section. Flip the box and
append today's date:

- Before: `- [ ] Digit Queries`
- After:  `- [x] Digit Queries — 2026-07-08`

Rules:
- Use today's actual date in `YYYY-MM-DD` format (check the current date; do not guess).
- Match the exact em-dash spacing already used: ` — ` (space, em-dash `—`, space).
- Only change the one line for the problem just solved. Don't touch other entries.
- The README name may differ from the folder name (folder `shortestRoutesII` →
  README `Shortest Routes II`). Grep the README to find the line.

Edit **only** the checkbox line. Do not hand-edit the progress table — step 3
regenerates it.

## 3. Recompute the progress table

```bash
python3 .claude/skills/solve-commit/update_progress.py
```

The checkboxes are the source of truth. This rewrites, from them, the Progress
Summary table and the `**N problems solved**` line.

It is idempotent and self-healing — if a count was ever wrong, this corrects it.

Use `--check` to see what would change without writing (exits 1 if anything is
stale). If it errors with *"no checkboxes under: X"*, a section heading was
renamed; fix the heading or update `SECTIONS` in the script.

Counts are solved-only — no denominators, no percentages. The CSES problem set
has no finish line worth tracking against, so don't reintroduce a Total column.

Only the sections named in `SECTIONS` count. The README's Interview Topic
Checklist, String Algorithms, and Weekly Schedule contain checkboxes that are
not solved problems, and are excluded.

## Solving a problem that isn't listed yet

The list grows. If the problem has no checklist line, add it as `- [x] Name —
YYYY-MM-DD` under the right topic section, then run step 3 normally — the count
picks it up. A brand-new topic section also needs an entry in `SECTIONS` in the
script and a matching row in the summary table, or its problems go uncounted.

## 4. Stage

Add the problem folder and the README:

```bash
git add Graph/flightDiscount/ README.md
```

Include every solution file (`.py`, `.cpp`, …) and a new `tests/` dir if there
is one. Never stage `__pycache__/`, `*.pyc`, `.DS_Store`, compiled binaries, or
scratchpad files — the root `.gitignore` covers the common ones. Check
`git status --short` before committing.

## 5. Commit

A single imperative summary line naming the solution and its key technique,
then the co-author trailer:

```text
Add flightDiscount solution (Dijkstra on doubled state graph, Python) and mark complete in README

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
```

- Start with `Add <folder> solution (<technique/notes>) and mark complete in README`.
- Name the algorithm; if several language versions exist, list them.
- Always end with the `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` trailer.

## 6. Push

```bash
git push
```

Remote is `origin` on `main`. If push is rejected for being behind, `git pull
--rebase` then push again — never force-push.

## Notes
- Committing and pushing are pre-authorized; no need to re-ask. This holds for
  any commit in this repo, not just solves — scaffolding, skill edits, and
  refactors get pushed too. Never leave commits sitting unpushed.
- `Sorting&Searching` has an `&` in the name; quote it in shell commands.
