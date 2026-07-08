class Node:
    def __init__(self, id):
        self.id = id
        self.children = []
        self.subOrds = 0

    def addChild(self, child):
        self.children.append(child)

    def getChildren(self):
        return self.children
    
    def setSub(self, subOrds):
        self.subOrds = subOrds

    def getSub(self):
        return self.subOrds

def postOrder(root):
    # Iterative post-order to avoid Python's recursion limit on deep trees.
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        stack.extend(node.getChildren())
    for node in reversed(order):
        count = sum(child.getSub() + 1 for child in node.getChildren())
        node.setSub(count)

if __name__ == "__main__":
    n = int(input())
    nodeList = [Node(i) for i in range(1, n + 1)]

    if n > 1:
        data = input().split()
        inpList = [int(x) for x in data]
        for idx, i in enumerate(inpList):
            nodeList[i - 1].addChild(nodeList[idx + 1])

    postOrder(nodeList[0])

    print(' '.join(str(node.getSub()) for node in nodeList) + ' ')