# 4 6 3
# 1 2 1
# 1 3 3
# 2 3 2
# 2 4 6
# 3 2 8
# 3 4 1
import heapq

if __name__ == "__main__":
    inp1 = input().split(' ')
    n,m,k = int(inp1[0]),int(inp1[1]),int(inp1[2])
    graph = dict()
    cntDict = dict()
    for i in range(n): 
        graph[i+1] = []
        cntDict[i+1] = 0

    for _ in range(m):
        inp2 = input().split(' ')
        e1,e2,w = int(inp2[0]),int(inp2[1]),int(inp2[2])
        graph[e1].append((w, e2))

    q = []
    heapq.heappush(q, (0, 1))
    resList = []

    while len(q) > 0:
        w, element = heapq.heappop(q)
        if cntDict[element] == k: continue
        cntDict[element] += 1
        if element == n: resList.append(w)
        for d, neighbor in graph[element]:
            heapq.heappush(q, (w + d, neighbor))

    print(*resList)
