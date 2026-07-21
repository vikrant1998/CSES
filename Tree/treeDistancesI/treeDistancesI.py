# 5
# 1 2
# 1 3
# 3 4
# 3 5

from collections import deque

def bfs(graph, start):
    q = deque()
    dist = [0] * (len(graph) + 1)
    q.append(start)
    visited = set()
    while len(q) > 0:
        element = q.popleft()
        visited.add(element)
        for neighbor in graph[element]:
            if neighbor not in visited:
                dist[neighbor] = dist[element] + 1
                visited.add(neighbor)
                q.append(neighbor)
        if len(q) == 0:
            return (element, dist)


if __name__ == "__main__":
    n = int(input())
    graph = dict()
    
    for i in range(1, n+1): 
        graph[i] = []
    
    for _ in range(n-1):
        inp1 = input().split(' ')
        e1, e2 = int(inp1[0]), int(inp1[1])
        graph[e1].append(e2)
        graph[e2].append(e1)

    node, dist = bfs(graph, 1)
    node1, dist1 = bfs(graph, node)
    node2, dist2 = bfs(graph, node1)

    finDist = [0] * (n+1)
    for i in range(1, n+1):
        finDist[i] = max(dist1[i], dist2[i])

    print(*finDist[1:])