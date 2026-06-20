from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.team = 0
        self.neighbors = []
    
    def addNeighbor(self, nodePtr):
        self.neighbors.append(nodePtr)

if __name__ == "__main__":
    inp1 = input().split(' ')
    v, e = int(inp1[0]), int(inp1[1])

    nodeList = [Node(0)]
    for i in range(1, v+1): nodeList.append(Node(i))

    for i in range(e):
        inp2 = input().split(' ')
        e1, e2 = int(inp2[0]), int(inp2[1])
        nodeList[e1].addNeighbor(nodeList[e2])
        nodeList[e2].addNeighbor(nodeList[e1])

    q = deque()
    impossible = False

    for i in range(1, v+1):
        if impossible == True:
            break

        if nodeList[i].team == 0:
            nodeList[i].team = 1
            q.append(nodeList[i])

        while len(q) > 0:
            if impossible == True: break
            popped = q.pop()
            for neighbor in popped.neighbors:
                if neighbor.team == 0:
                    neighbor.team = 2 if popped.team == 1 else 1
                    q.append(neighbor)
                else:
                    if neighbor.team == popped.team:
                        impossible = True
                        break

    if impossible == True:
        print('IMPOSSIBLE')
    else:
        for i in range(1, v+1):
            print(nodeList[i].team)
