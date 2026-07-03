# Input:

# 8 3
# 3 6 2
# Output:

# 5 3 3

class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, nodePtr):
        if self.head == None and self.tail == None:
            self.head = nodePtr
            self.tail = nodePtr
        else:
            self.tail.next = nodePtr
            nodePtr.prev = self.tail
            self.tail = nodePtr

    def deleteNode(self, nodePtr):
        if nodePtr.prev == None and nodePtr.next == None:
            self.head = None
            self.tail = None
        elif nodePtr.prev == None:
            nodePtr.next.prev = None
            self.head = nodePtr.next
        elif nodePtr.next == None:
            nodePtr.prev.next = None
            self.tail = nodePtr.prev
        else:
            nodePtr.prev.next = nodePtr.next
            nodePtr.next.prev = nodePtr.prev

        del nodePtr

if __name__ == "__main__":
    inp1 = input().split(' ')
    sSize, splits = int(inp1[0]), int(inp1[1])
    inp2 = input().split(' ')
    inpList = [(idx, int(x)) for idx, x in enumerate(inp2)]

    import copy
    sortedList = copy.deepcopy(inpList)
    sortedList.sort(key = lambda x: x[1])

    nodeMap = dict()
    for inp in inpList: nodeMap[inp[0]] = Node(inp[1])

    # Build the DLL with ALL lights present, plus the two road endpoints
    # (positions 0 and sSize) as sentinel nodes so every real light always
    # has a left and right neighbor. Nodes go in sorted-by-position order,
    # so neighbors in the list are neighbors on the road.
    dll = DoublyLinkedList()
    dll.addNode(Node(0))                       # left endpoint
    for s in sortedList:
        dll.addNode(nodeMap[s[0]])
    dll.addNode(Node(sSize))                   # right endpoint

    # Max gap with every light present: scan consecutive positions once.
    gMax = 0
    cur = dll.head
    while cur.next:
        gMax = max(gMax, cur.next.val - cur.val)
        cur = cur.next

    # Remove lights in REVERSE of the order they were added. Removing a light
    # merges its two neighboring gaps into one: right.val - left.val. The max
    # gap only grows as lights disappear, so gMax stays a running maximum.
    # We record the max BEFORE each removal (that's the answer for the state
    # with this many lights still present), then reverse the answers at the end.
    answers = []
    for inp in inpList[::-1]:
        answers.append(gMax)
        nodePtr = nodeMap[inp[0]]
        l = nodePtr.prev.val                   # always defined thanks to sentinels
        r = nodePtr.next.val
        gMax = max(gMax, r - l)
        dll.deleteNode(nodePtr)

    print(' '.join(str(a) for a in answers[::-1]) + ' ')