---
name: solve-commit
description: Finalize a solved NeetCode problem — mark it complete in README.md with today's date, stage the solution, commit with the project's message convention, and push. Use whenever the user says a problem is solved/passing and wants it recorded, committed, or pushed (for example, "add to git", "commit this solution", or "mark X done and push").
---

# Finalize a solved NeetCode problem

When a NeetCode problem's solution passes and the user wants it recorded, do these steps in order.

## 1. Mark it complete in README.md

Each problem is a checklist line under its category section in `NeetCode150/README.md`. Flip the box and append today's date:

- Before: `- [ ] Valid Anagram`
- After:  `- [x] Valid Anagram — 2026-07-08`

Rules:
- Use today's actual date in `YYYY-MM-DD` format (check the current date; do not guess).
- Match the exact em-dash spacing already used: ` — ` (space, em-dash `—`, space).
- Only change the one line for the problem just solved. Don't touch other entries.
- The README problem name may differ from the folder name (e.g. folder `containsDuplicate` → README `Contains Duplicate`). Grep the README for the problem to find its line.
- Also bump the Progress Summary table: increment the category's `Solved` count and the `Total` row.

## 2. Stage the solution

Add the problem folder and any newly created solution files, plus the README:

```bash
git add NeetCode150/containsDuplicate/ NeetCode150/README.md
```

Include every solution file the user created (for example, `.py` or `.cpp`) and any new test assets if relevant. Do not add scratchpad or temporary files.

## 3. Commit with the project convention

Use a single imperative summary line that names the solution and the core technique, then end with the co-author trailer.

Example:

```text
Add containsDuplicate solution (hash set, Python) and mark complete in README

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
```

Rules:
- Start with `Add <folder> solution (<technique/notes>) and mark complete in README`.
- Mention the algorithm and, if multiple language versions exist, list them.
- Always end with the `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` trailer.

## 4. Push

```bash
git push
```

The remote is `origin` on the current branch. If push is rejected for being behind, pull with rebase (`git pull --rebase`) and push again rather than force-pushing.

## Notes
- Committing and pushing here is expected and pre-authorized by this workflow; you do not need to re-ask each time the user invokes this.
- If tests have not been run or verified in the session, run them before committing rather than assuming they pass.
