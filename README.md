# Competitive Programming / Interview Prep

Two tracks, worked in parallel. CSES builds algorithmic depth; NeetCode 150 drills
the patterns that actually show up in interviews.

For every problem, write down:
- What is the idea?
- What data structure/algorithm is being used?
- Why is the time complexity accepted?
- What mistake did I make?

---

## Overall Progress

| Track | Solved | Total | Progress |
|-------|--------|-------|----------|
| [CSES Problem Set](CSES/README.md) | 58 | 117 | 50% |
| [NeetCode 150](NeetCode150/README.md) | 1 | 150 | 1% |
| **Combined** | **59** | **267** | **22%** |

---

## [CSES](CSES/README.md)

Main resource: [CSES Problem Set](https://cses.fi/problemset/)

| Topic | Solved | Total |
|-------|--------|-------|
| Introductory | 18 | 19 |
| Sorting and Searching | 15 | 28 |
| Dynamic Programming | 10 | 20 |
| Graph Algorithms | 11 | 22 |
| Tree Algorithms | 2 | 14 |
| Range Queries | 2 | 14 |
| **Total** | **58** | **117** |

The CSES README also carries an Interview Topic Checklist, String Algorithms,
and a Weekly Schedule; those aren't problem counts and are excluded here.

---

## [NeetCode 150](NeetCode150/README.md)

Main resource: [NeetCode 150](https://neetcode.io/practice)

| Topic | Solved | Total |
|-------|--------|-------|
| Arrays & Hashing | 1 | 9 |
| Two Pointers | 0 | 5 |
| Sliding Window | 0 | 6 |
| Stack | 0 | 7 |
| Binary Search | 0 | 7 |
| Linked List | 0 | 11 |
| Trees | 0 | 15 |
| Tries | 0 | 3 |
| Heap / Priority Queue | 0 | 7 |
| Backtracking | 0 | 9 |
| Graphs | 0 | 13 |
| Advanced Graphs | 0 | 6 |
| 1-D Dynamic Programming | 0 | 12 |
| 2-D Dynamic Programming | 0 | 11 |
| Greedy | 0 | 8 |
| Intervals | 0 | 6 |
| Math & Geometry | 0 | 8 |
| Bit Manipulation | 0 | 7 |
| **Total** | **1** | **150** |

---

## Layout

```
CSES/          # solutions grouped by topic, README.md is the checklist
NeetCode150/   # one folder per problem, README.md is the checklist
```

Each track has a directory-scoped `solve-commit` skill under `.claude/skills/`
that marks a problem complete in that track's README, commits, and pushes.
Per-problem checkboxes and dates live in the track READMEs; this file only
carries the roll-up counts.
