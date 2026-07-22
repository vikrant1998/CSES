# 200-Day Programming / Interview Prep Roadmap

Goal: become strong enough for technical interviews in ~200 days.

Main resource: [CSES Problem Set](https://cses.fi/problemset/)  
Rule: do not rush. For every problem, write down:
- What is the idea?
- What data structure/algorithm is being used?
- Why is the time complexity accepted?
- What mistake did I make?

---

## Progress Summary

**71 problems solved** (one solution folder each on disk).

| Topic | Solved |
|-------|--------|
| Introductory | 19 |
| Sorting and Searching | 21 |
| Dynamic Programming | 10 |
| Graph Algorithms | 14 |
| Tree Algorithms | 4 |
| Range Queries | 2 |
| String Algorithms | 1 |
| **Total** | **71** |

Every solved problem is checked off `[x]` in its phase section below. Counts are
solved-only — there's no fixed target to finish, just more problems.

---

## Layout

```
Introductory/          # one folder per problem, plus tests/ where CSES gives them
Sorting&Searching/
DynamicProgramming/
Graph/
Tree/
RangeQueries/
check.sh               # ./check.sh solution.py [tests_dir] — diffs against tests/*.out
```

A `solve-commit` skill under `.claude/skills/` marks a problem complete here,
regenerates the table above from the checkboxes, commits, and pushes.

---

# Phase 1 — Foundations: Intro + Sorting / Searching

Target: Days 1–30

Focus:
- loops
- sorting
- greedy
- two pointers
- maps / sets
- binary search
- implementation speed

## Introductory Problems

- [x] Weird Algorithm — 2026-05-28
- [x] Missing Number — 2026-05-28
- [x] Repetitions — 2026-05-28
- [x] Increasing Array — 2026-05-28
- [x] Permutations — 2026-05-28
- [x] Number Spiral — 2026-05-29
- [x] Two Knights — 2026-05-28
- [x] Two Sets — 2026-05-29
- [x] Bit Strings — 2026-05-28
- [x] Trailing Zeros — 2026-05-28
- [x] Coin Piles — 2026-05-31
- [x] Palindrome Reorder — 2026-05-31
- [x] Gray Code — 2026-06-02
- [x] Tower of Hanoi — 2026-06-03
- [x] Creating Strings — 2026-06-03
- [x] Apple Division — 2026-06-05
- [x] Chessboard and Queens — 2026-06-06
- [x] Digit Queries — 2026-07-14
- [x] Grid Path Description — 2026-06-06

## Sorting and Searching

- [x] Distinct Numbers — 2026-05-28
- [x] Sum of Two Values — 2026-05-30
- [x] Maximum Subarray Sum — 2026-05-28
- [x] Apartments — 2026-06-03
- [x] Ferris Wheel — 2026-06-07
- [x] Concert Tickets — 2026-06-07
- [x] Restaurant Customers — 2026-06-09
- [x] Movie Festival — 2026-06-10
- [x] Stick Lengths — 2026-06-10
- [x] Missing Coin Sum — 2026-06-11
- [x] Collecting Numbers — 2026-06-11
- [x] Collecting Numbers II — 2026-06-22
- [x] Playlist — 2026-06-24
- [x] Towers — 2026-06-28
- [x] Traffic Lights — 2026-07-02
- [x] Distinct Values Subarrays — 2026-07-11
- [x] Distinct Values Subsequences — 2026-07-12
- [x] Josephus Problem I — 2026-07-11
- [ ] Room Allocation
- [ ] Factory Machines
- [ ] Tasks and Deadlines
- [ ] Reading Books
- [x] Sum of Three Values — 2026-07-13
- [x] Sum of Four Values — 2026-07-13
- [x] Nearest Smaller Values — 2026-07-21
- [ ] Subarray Sums I
- [ ] Subarray Sums II
- [ ] Subarray Divisibility
- [ ] Array Division
- [ ] Movie Festival II
- [ ] Maximum Subarray Sum II

---

# Phase 2 — Dynamic Programming

Target: Days 31–75

Focus:
- defining `dp[i]`
- base cases
- transitions
- computing order
- modulo arithmetic
- 1D DP
- 2D DP
- knapsack-style DP
- interval DP

## Dynamic Programming Problems

- [x] Dice Combinations — 2026-05-28
- [x] Minimizing Coins — 2026-06-12
- [x] Coin Combinations I — 2026-06-13
- [x] Coin Combinations II — 2026-06-15
- [x] Removing Digits — 2026-06-15
- [x] Grid Paths I — 2026-06-16
- [x] Book Shop — 2026-06-20
- [ ] Array Description
- [ ] Counting Towers
- [x] Edit Distance — 2026-07-01
- [x] Longest Common Subsequence — 2026-07-02
- [ ] Rectangle Cutting
- [ ] Money Sums
- [ ] Removal Game
- [ ] Two Sets II
- [x] Increasing Subsequence — 2026-07-01
- [ ] Projects
- [ ] Elevator Rides
- [ ] Counting Tilings
- [ ] Counting Numbers

---

# Phase 3 — Graph Algorithms

Target: Days 76–115

Focus:
- DFS
- BFS
- connected components
- shortest path
- bipartite graphs
- cycle detection
- topological sorting
- Dijkstra
- Bellman-Ford
- MST

## Graph Algorithms Problems

- [x] Counting Rooms — 2026-05-30
- [x] Labyrinth — 2026-05-30
- [x] Building Roads — 2026-06-08
- [x] Message Route — 2026-06-09
- [x] Building Teams — 2026-06-20
- [x] Round Trip — 2026-07-04
- [x] Monsters — 2026-07-07
- [x] Shortest Routes I — 2026-07-04
- [x] Shortest Routes II — 2026-07-04
- [x] High Score — 2026-07-04
- [x] Flight Discount — 2026-07-08
- [x] Cycle Finding — 2026-07-08
- [x] Flight Routes — 2026-07-08
- [ ] Round Trip II
- [x] Course Schedule — 2026-07-11
- [ ] Longest Flight Route
- [ ] Game Routes
- [ ] Investigation
- [ ] Road Reparation
- [ ] Road Construction
- [ ] Flight Routes Check
- [ ] Planets and Kingdoms

---

# Phase 4 — Range Queries + Trees

Target: Days 116–150

Focus:
- prefix sums
- segment trees
- Fenwick trees
- binary lifting
- tree DFS
- subtree queries
- path queries
- LCA

## Range Queries

- [x] Static Range Sum Queries — 2026-06-17
- [x] Static Range Minimum Queries — 2026-06-20
- [ ] Dynamic Range Sum Queries
- [ ] Dynamic Range Minimum Queries
- [ ] Range Xor Queries
- [ ] Range Update Queries
- [ ] Forest Queries
- [ ] Hotel Queries
- [ ] List Removals
- [ ] Salary Queries
- [ ] Prefix Sum Queries
- [ ] Pizzeria Queries
- [ ] Subarray Sum Queries
- [ ] Distinct Values Queries

## Tree Algorithms

- [x] Tree Matching — 2026-07-18
- [x] Subordinates — 2026-05-30
- [x] Tree Diameter — 2026-05-31
- [x] Tree Distances I — 2026-07-20
- [ ] Tree Distances II
- [ ] Company Queries I
- [ ] Company Queries II
- [ ] Distance Queries
- [ ] Counting Paths
- [ ] Subtree Queries
- [ ] Path Queries
- [ ] Path Queries II
- [ ] Distinct Colors
- [ ] Finding a Centroid

---

# Phase 5 — String Algorithms

Target: Days 151–170

Focus:
- string matching
- hashing
- tries
- KMP
- Z algorithm
- suffix arrays/basic suffix concepts

Important: come back to `Word Combinations` here, not earlier.

## String Algorithms

- [x] String Matching — 2026-07-08
- [ ] Finding Borders
- [ ] Finding Periods
- [ ] Minimal Rotation
- [ ] Longest Palindrome
- [ ] Word Combinations
- [ ] Finding Patterns
- [ ] Counting Patterns
- [ ] Pattern Positions
- [ ] Distinct Substrings
- [ ] Distinct Subsequences
- [ ] Repeating Substring
- [ ] String Functions

---

# Phase 6 — Interview Mode

Target: Days 171–200

Focus:
- explaining while coding
- solving under time pressure
- clean implementation
- recognizing patterns quickly
- reviewing mistakes

## Weekly Schedule

- [ ] 3 days: LeetCode-style interview problems
- [ ] 2 days: CSES maintenance / harder problems
- [ ] 1 day: timed mock interview
- [ ] 1 day: review old mistakes

## Interview Topic Checklist

### Arrays / Strings

- [ ] Two Sum
- [ ] Best Time to Buy and Sell Stock
- [ ] Product of Array Except Self
- [ ] Maximum Subarray
- [ ] Merge Intervals
- [ ] Insert Interval
- [ ] Rotate Array
- [ ] Valid Anagram
- [ ] Group Anagrams
- [ ] Longest Substring Without Repeating Characters

### Two Pointers / Sliding Window

- [ ] Valid Palindrome
- [ ] Container With Most Water
- [ ] 3Sum
- [ ] Minimum Window Substring
- [ ] Longest Repeating Character Replacement
- [ ] Sliding Window Maximum

### Hash Maps / Sets

- [ ] Contains Duplicate
- [ ] Top K Frequent Elements
- [ ] Subarray Sum Equals K
- [ ] Longest Consecutive Sequence

### Stack / Queue

- [ ] Valid Parentheses
- [ ] Min Stack
- [ ] Daily Temperatures
- [ ] Evaluate Reverse Polish Notation
- [ ] Largest Rectangle in Histogram

### Binary Search

- [ ] Binary Search
- [ ] Search in Rotated Sorted Array
- [ ] Find Minimum in Rotated Sorted Array
- [ ] Koko Eating Bananas
- [ ] Median of Two Sorted Arrays

### Linked Lists

- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Linked List Cycle
- [ ] Remove Nth Node From End
- [ ] Reorder List
- [ ] LRU Cache

### Trees

- [ ] Invert Binary Tree
- [ ] Maximum Depth of Binary Tree
- [ ] Diameter of Binary Tree
- [ ] Balanced Binary Tree
- [ ] Same Tree
- [ ] Subtree of Another Tree
- [ ] Lowest Common Ancestor
- [ ] Binary Tree Level Order Traversal
- [ ] Validate Binary Search Tree
- [ ] Kth Smallest Element in BST

### Graphs

- [ ] Number of Islands
- [ ] Clone Graph
- [ ] Pacific Atlantic Water Flow
- [ ] Course Schedule
- [ ] Rotting Oranges
- [ ] Word Ladder
- [ ] Network Delay Time
- [ ] Redundant Connection

### Dynamic Programming

- [ ] Climbing Stairs
- [ ] House Robber
- [ ] House Robber II
- [ ] Coin Change
- [ ] Longest Increasing Subsequence
- [ ] Longest Common Subsequence
- [ ] Word Break
- [ ] Combination Sum IV
- [ ] Unique Paths
- [ ] Decode Ways
- [ ] Partition Equal Subset Sum

### Backtracking

- [ ] Subsets
- [ ] Combination Sum
- [ ] Permutations
- [ ] Letter Combinations of a Phone Number
- [ ] Word Search
- [ ] N-Queens

### Heaps

- [ ] Kth Largest Element in an Array
- [ ] Last Stone Weight
- [ ] K Closest Points to Origin
- [ ] Task Scheduler
- [ ] Find Median from Data Stream

---

# Daily Template

```txt
Date:

Problem:

Topic:

Status:
- [ ] Solved alone
- [ ] Needed hint
- [ ] Read editorial
- [ ] Re-solved later

Idea:


Mistake:


Time Complexity:


Space Complexity:


What I learned:
