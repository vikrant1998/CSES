# Input:
# 5
# 1 2
# 1 3
# 3 4
# 3 5

# Output:
# 2
from collections import deque

if __name__ == "__main__":
    n = int(input())
    graph = dict()
    inEdges = dict()
    for i in range(n):
        graph[i + 1] = []
        inEdges[i + 1] = 0

    for _ in range(n - 1):
        inp1 = input().split()
        e1, e2 = int(inp1[0]), int(inp1[1])
        graph[e1].append(e2)
        graph[e2].append(e1)
        inEdges[e1] += 1
        inEdges[e2] += 1

    q = deque()
    for i in range(n):
        if inEdges[i + 1] == 1:
            q.append(i + 1)

    paired = set()
    count = 0
    while len(q) > 0:
        node = q.popleft()

        # A node may already be in the queue after its only edge was removed
        # by another leaf, so process it only if it is still an active leaf.
        if inEdges[node] != 1:
            continue

        for neighbor in graph[node]:
            # Ignore edges that were already removed during leaf processing.
            if inEdges[neighbor] == 0:
                continue

            # A matching edge can be selected only when neither endpoint has
            # already been used. Each endpoint is then paired exactly once.
            if node not in paired and neighbor not in paired:
                count += 1
                paired.add(node)
                paired.add(neighbor)

            # Remove this leaf edge from the active tree.
            inEdges[node] -= 1
            inEdges[neighbor] -= 1
            if inEdges[neighbor] == 1:
                q.append(neighbor)

            # Since node was an active leaf, it had only this active neighbor.
            break

    print(count)
