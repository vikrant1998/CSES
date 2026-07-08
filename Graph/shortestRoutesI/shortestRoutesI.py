# 3 4
# 1 2 6
# 1 3 2
# 3 2 3
# 1 3 4

import heapq

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, m = int(inp1[0]), int(inp1[1])
    graph = dict()
    for i in range(n): graph[i+1] = []

    for i in range(m):
        inp2 = input().split(' ')
        a, b, w = int(inp2[0]), int(inp2[1]), int(inp2[2])
        graph[a].append((w, b))

    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    q = []
    heapq.heappush(q, (0, 1))

    while len(q) > 0:
        d, element = heapq.heappop(q)
        if d > dist[element]:
            continue

        for weight, neighbor in graph[element]:
            if d + weight < dist[neighbor]:
                dist[neighbor] = d + weight
                heapq.heappush(q, (d + weight, neighbor))

    print(' '.join(str(dist[i]) for i in range(1, n + 1)) + ' ')


