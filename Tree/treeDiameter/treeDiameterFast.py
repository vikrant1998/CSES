# Fast CSES-passing version of Tree Diameter.
# Uses the two-BFS trick instead of recursion, so there is no call-stack
# depth limit and no need for a big thread stack.
#
# Why two BFS:
#   1. BFS from any node -> the farthest node you reach (call it u) is
#      guaranteed to be one endpoint of some longest path (the diameter).
#   2. BFS again from u -> the farthest distance is the diameter itself.
#
# See treeDiameter.py for the recursive post-order version (kept for learning).

import sys
from collections import deque

def bfs(start, adj, n):
    """Return (farthest_node, distance_to_it) from `start`."""
    dist = [-1] * (n + 1)
    dist[start] = 0
    far = start
    q = deque([start])
    while q:
        u = q.popleft()
        du = dist[u]
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = du + 1
                if dist[v] > dist[far]:
                    far = v
                q.append(v)
    return far, dist[far]

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        adj[a].append(b)
        adj[b].append(a)

    if n <= 1:
        print(0)
        return

    u, _ = bfs(1, adj, n)          # step 1: find one endpoint
    _, diameter = bfs(u, adj, n)   # step 2: farthest from it = diameter
    print(diameter)

if __name__ == "__main__":
    main()
