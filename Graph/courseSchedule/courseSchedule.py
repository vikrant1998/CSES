# Input:
# 5 3
# 1 2
# 3 1
# 4 5

# Output:
# 3 4 1 5 2

from collections import deque

if __name__ == "__main__":
    inp1 = input().split(' ')
    v, e = int(inp1[0]), int(inp1[1])

    graph = dict()
    inEdges = dict()
    for i in range(v):
        graph[i+1] = []
        inEdges[i+1] = 0

    for _ in range(e):
        inp2 = input().split(' ')
        e1, e2 = int(inp2[0]), int(inp2[1])
        graph[e1].append(e2)
        inEdges[e2] += 1

    q = deque()

    # Start q with all nodes with in-edges 0
    for i in range(v):
        if inEdges[i+1] == 0:
            q.append(i+1)

    finList = []
    while len(q) > 0:
        element = q.popleft()
        finList.append(element)

        for neighbor in graph[element]:
            inEdges[neighbor] -= 1
            if inEdges[neighbor] == 0:
                q.append(neighbor)

    for i in range(v):
        if inEdges[i+1] > 0:
            print('IMPOSSIBLE')
            exit()

    print(' '.join(map(str, finList)))

    