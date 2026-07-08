class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self

    def addParent(self, nodePtr):
        self.parent = nodePtr

    def findParent(self):
        if self.parent != self:
            self.parent = self.parent.findParent()
        return self.parent

if __name__ == "__main__":
    inpStr = input().split(' ')
    n, m = int(inpStr[0]), int(inpStr[1])
    nodeMap = dict()
    for i in range(n): nodeMap[i + 1] = Node(i + 1)

    i = 0
    while i < m:
        eStr = input().split(' ')
        e1, e2 = int(eStr[0]), int(eStr[1])

        nodeMap[e1].findParent().addParent(nodeMap[e2].findParent())
        i += 1

    pSet = set()
    for i in range(n):
        pSet.add(nodeMap[i+1].findParent().val)

    pList = list(pSet)
    i = 0

    print(len(pList) - 1)
    while i < len(pList) and (i + 1) < len(pList):
        print(str(pList[i]) + ' ' + str(pList[i + 1]))
        i += 1
