from collections import deque
import sys
import threading
sys.setrecursionlimit(300000)


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.diameter = 0
    
    def addChild(self, nodePtr):
        self.children.append(nodePtr)

def postOrder(root, parent):
    height = 0
    max1 = 0
    max2 = 0
    for c in root.children:
        if c is parent:
            continue
        h = postOrder(c, root)
        if h > max1:
            max2 = max1
            max1 = h
        elif h > max2:
            max2 = h
        height = max(h, height)
    root.diameter = max1 + max2
    return height + 1

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1

    nodeList = [Node(x) for x in range(1, n + 1)]

    for i in range(n - 1):
        rootVal = int(data[idx]); nodeVal = int(data[idx + 1]); idx += 2
        nodeList[rootVal - 1].addChild(nodeList[nodeVal - 1])
        nodeList[nodeVal - 1].addChild(nodeList[rootVal - 1])

    postOrder(nodeList[0], nodeList[0])
    maxVal = 0
    for nodePtr in nodeList:
        maxVal = max(maxVal, nodePtr.diameter)
    print(maxVal)

if __name__ == "__main__":
    threading.stack_size(256 * 1024 * 1024)  # 256 MB stack
    threading.Thread(target=main).start()

