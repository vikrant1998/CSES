# Competitive Programming Progress Tracking

Use these instructions for all progress checks, solve logging, and debugging work in this repository.

Use the personal `$competitive-programming-coach` skill for live progress checks, readiness reassessments, new-submission reviews, and next-problem recommendations.

Also use that skill for Hello Interview system-design progress and readiness checks. Treat `SYSTEM_DESIGN_PROGRESS.md` as the manual source of truth. Keep reading coverage separate from independent design and mock-interview evidence.

## Goal And Plan

- Challenge start: 2026-05-28
- Duration: 200 days
- Tracks: CSES problem-set spine and NeetCode 150
- System-design track: all core Hello Interview question breakdowns, tracked in `SYSTEM_DESIGN_PROGRESS.md`
- AI FDE curriculum: follow the ordered `ai-system-design-guide` checklist in `SYSTEM_DESIGN_PROGRESS.md`
- Primary long-term goal: Google FDE interview readiness
- Maintain Google SDE-level algorithms, data structures, coding, and problem-solving ability even though FDE is the target role.
- Compute the current challenge day from the start date; do not store a remembered day number as current.

## Live Sources Of Truth

Never use self-reported, remembered, or previously summarized solve counts when a live check is requested.

### CSES

- Repository: `https://github.com/vikrant1998/CSES`
- Fetch the raw README from `https://raw.githubusercontent.com/vikrant1998/CSES/main/README.md?nocache=<timestamp>`.
- When checking immediately after a reported push, compare `refs/heads/main` and use a fresh shallow clone if the raw README endpoint has not caught up.
- Count `- [x]` and `- [ ]` checkboxes within each problem section.
- Use the solve dates appended as `— YYYY-MM-DD` when reporting recent activity.
- The six core sections contain 120 problems: Introductory, Sorting and Searching, Dynamic Programming, Graph Algorithms, Tree Algorithms, and Range Queries.
- String Algorithms contains 13 additional problems. Report it separately so the 120-problem core denominator is not confused with all 133 tracked checkboxes.
- The README summary includes solved String problems in its total. State clearly whether a number is the README total or the six-section core total.

### NeetCode

- Repository: `https://github.com/vikrant1998/neetcode-submissions`
- Shallow-clone the repository into a temporary directory with `git clone --depth 5`.
- Solve count is the number of problem directories exactly one level beneath `Data Structures & Algorithms/`.
- Do not use the unauthenticated GitHub API when a shallow clone is available.

If either repository cannot be reached, state that verification failed. Do not extrapolate a count.

## Progress Check Output

- Give verified numbers and section breakdowns, followed by a few plain-English sentences explaining how progress is going.
- Include a brief, specific, and grounded motivational note on every progress check.
- Do not add unsolicited schedules or problem recommendations.
- Include the current challenge day, verified CSES count, verified NeetCode count, combined count, and solve pace calculated from live totals.
- Include CSES solved/total by section from the live README.
- Include Hello Interview core breakdowns read out of 30, independent designs completed, and timed/peer mocks completed from `SYSTEM_DESIGN_PROGRESS.md`.
- Evaluate coding readiness and applied system-design readiness separately. Use both when explaining progress toward Google FDE readiness, but do not treat reading coverage as proof of design ability.
- Flag the open tracking items below after the numeric report.
- Keep the report concise.

After each newly detected submission, reassess readiness from the actual cumulative solved set and representative code. Do not base the score on the user's self-analysis or manually tracked backlog. Recommend 2-4 unsolved CSES or NeetCode problems that extend demonstrated prerequisites and address the most valuable Google FDE/SDE interview gaps. Prioritize common interview patterns over competitive-programming-specialized topics such as Fenwick trees, segment trees, SCC, or advanced DP unless those prerequisites and higher-priority patterns are already covered.

## Open Tracking Items

- Write-up backlog: approximately 11-13 problems; flag it on every check until updated.
- NeetCode Tries: 1/3; Implement Prefix Tree is complete, with Design Add and Search Words and Word Search II remaining.
- Distinct Values: re-solve window around 2026-07-25 through 2026-07-28.
- Find Duplicate Integer: solved using O(n) space; O(1) Floyd cycle-detection redo remains pending.

These items are manually tracked context, not verified solve counts. Do not silently mark them complete. Update them only from an explicit user statement or clear repository evidence.

## Debugging Preference

- Give a hint first, not the fix.
- Provide the direct fix only when explicitly requested.
- Preserve the user's approach where possible and explain the failing invariant or edge case before proposing replacement code.

## Last Verified Snapshot

This snapshot is historical context only. Refresh both repositories before presenting current progress.

- Verified: 2026-07-23
- Challenge day: 57
- CSES README total: 71
- NeetCode: 54
- Combined: 125
- CSES breakdown: Introductory 19, Sorting and Searching 21, Dynamic Programming 10, Graph Algorithms 14, Tree Algorithms 4, Range Queries 2, String Algorithms 1
