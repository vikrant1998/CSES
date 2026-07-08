# 3 4
# 1 2 3
# 2 3 1
# 1 3 7
# 2 1 5

import heapq

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, e = int(inp1[0]), int(inp1[1])

    graph = dict()
    for i in range(n): graph[i+1] = []

    for _ in range(e):
        inp2 = input().split(' ')
        e1, e2, w = int(inp2[0]), int(inp2[1]), int(inp2[2])
        graph[e1].append((w, e2))

    q = []
    dist = [[float('inf') for _ in range(n+1)] for _ in range(2)]
    heapq.heappush(q, (0, 1, 0))

    while len(q) > 0:
        d, element, used = heapq.heappop(q)
        if d > dist[used][element]: continue

        for w, neighbor in graph[element]:
            if d + w < dist[used][neighbor]:
                dist[used][neighbor] = d + w
                heapq.heappush(q, (d + w, neighbor, used))
            if used == 0 and d + (w // 2) < dist[1][neighbor]:
                dist[1][neighbor] = d + (w // 2)
                heapq.heappush(q, (d + (w // 2), neighbor, 1))

    print(min(dist[0][n], dist[1][n]))