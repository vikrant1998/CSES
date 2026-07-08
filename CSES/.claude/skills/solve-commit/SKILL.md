---
name: solve-commit
description: Finalize a solved CSES problem — mark it complete in README.md with today's date, git add the solution, commit with the project's message convention, and push. Use whenever the user says a problem is solved/passing and wants it recorded, committed, or pushed (e.g. "add to git and update readme", "commit this solution", "mark X done and push").
---

# Finalize a solved CSES problem

When a CSES problem's solution passes and the user wants it recorded, do these steps in order.

## 1. Mark it complete in README.md

Each problem is a checklist line under its section. Flip the box and append today's date:

- Before: `- [ ] Shortest Routes II`
- After:  `- [x] Shortest Routes II — 2026-07-04`

Rules:
- Use today's actual date in `YYYY-MM-DD` format (check the current date; do not guess).
- Match the exact em-dash spacing already used: ` — ` (space, em-dash `—`, space).
- Only change the one line for the problem just solved. Don't touch other entries.
- The README problem name may differ slightly from the folder name (e.g. folder `shortestRoutesII` → README `Shortest Routes II`). Grep the README for the problem to find its line.

## 2. Stage the solution

Add the problem's folder (or specific new files) plus the README:

```
git add Graph/shortestRoutesII/ README.md
```

Include every solution file the user created (`.py`, `.cpp`, etc.) and the `tests/` dir if it's new. Do not add scratchpad/temp files or compiled binaries.

## 3. Commit with the project convention

Message format (see `git log`): a single imperative summary line naming the solution and its key technique, then the co-author trailer.

```
Add shortestRoutesII solution (Floyd-Warshall, C++ + Python) and mark complete in README

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
```

- Summary starts with `Add <folder> solution (<technique/notes>) and mark complete in README`.
- Mention the algorithm and, if multiple language versions exist, list them.
- Always end with the `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` trailer.

## 4. Push

```
git push
```

The remote is `origin` on branch `main`. If push is rejected for being behind, pull with rebase (`git pull --rebase`) then push again — don't force-push.

## Notes
- Committing and pushing here is expected and pre-authorized by this workflow; you don't need to re-ask each time the user invokes this.
- If tests haven't actually been run/verified in the session, run them before committing rather than assuming they pass.
