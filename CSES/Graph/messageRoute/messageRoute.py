from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def addNeighbor(self, nodePtr):
        self.neighbors.append(nodePtr)

if __name__ == "__main__":
    inpStr = input().split(' ')
    n, m = int(inpStr[0]), int(inpStr[1])
    nodeList = [Node(x) for x in range(n+1)]

    for i in range(m):
        inp1 = input().split(' ')
        e1, e2 = int(inp1[0]), int(inp1[1])
        nodeList[e1].addNeighbor(nodeList[e2])
        nodeList[e2].addNeighbor(nodeList[e1])

    q = deque()
    q.append(nodeList[1])
    visited = set()
    visited.add(nodeList[1])
    pathFound = False
    pathMap = dict()
    pathMap[nodeList[1]] = None

    while len(q) > 0:
        topQ = q.popleft()

        if topQ.val == n:
            pathFound = True
            break

        for neighbor in topQ.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                pathMap[neighbor] = topQ

    stackPath = []
    if pathFound:
        track = nodeList[n]
        while track != None:
            stackPath.append(track.val)
            track = pathMap[track]
        stackPath = stackPath[::-1]
        print(len(stackPath))
        print(' '.join(map(str, stackPath)))
    else:
        print('IMPOSSIBLE')
