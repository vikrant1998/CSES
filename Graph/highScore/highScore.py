# 4 5
# 1 2 3
# 2 4 -1
# 1 3 -2
# 3 4 7
# 1 4 4

from collections import deque

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, m = int(inp1[0]), int(inp1[1])
    graph = [[float('inf')] * (n+1) for _ in range(n+1)]
    bfs_graph = dict()
    for i in range(1,n+1): bfs_graph[i] = []

    for i in range(m):
        inp2 = input().split(' ')
        e1, e2, w = int(inp2[0]), int(inp2[1]), int(inp2[2])
        graph[e1][e2] = min(-w, graph[e1][e2])
        bfs_graph[e2].append(e1)

    visited = set()
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    for _ in range(n-1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[j] = min(dist[j], dist[i] + graph[i][j])

    import copy
    negCheck = copy.deepcopy(dist)

    for _ in range(n-1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                negCheck[j] = min(negCheck[j], negCheck[i] + graph[i][j])

    corrupted = set()
    
    for i in range(1, n+1):
        if dist[i] != negCheck[i]:
            corrupted.add(i)

    joever = n in corrupted

    if joever:
        print(-1)
    else:
        print(-1 * dist[n])

    