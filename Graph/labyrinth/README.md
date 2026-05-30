# Labyrinth

[CSES Problem Set — Labyrinth](https://cses.fi/problemset/task/1193)

Given an `n × m` grid (`.` floor, `#` wall, `A` start, `B` end), find a shortest
path from `A` to `B` and print one such path.

## Approach

BFS from `A`. Since every move has equal cost, the first time BFS reaches `B`
it has found a shortest path. For each cell we store the parent cell and the
direction (`U`/`D`/`L`/`R`) used to reach it, then reconstruct the path by
walking parents back from `B`.

Cells are marked visited **when enqueued**, not when dequeued, so each cell
enters the queue at most once — keeping the BFS `O(n·m)`.

## Implementation notes

- The grid is flattened to a 1D `bytearray` (`idx = i*m + j`) to avoid the
  overhead of `(i, j)` tuples and a dict-keyed parent map.
- Parent index and parent direction are kept in flat lists/`bytearray`, giving
  O(1) array access instead of dict hashing.
- Input is read in one `sys.stdin.buffer.read()`; output is batched.

Runs the worst case (1000×1000 open grid) in well under the time limit.
