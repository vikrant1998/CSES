class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, nodePtr):
        if self.head == None and self.tail == None:
            self.head = nodePtr
            self.tail = nodePtr
            nodePtr.next = nodePtr
            nodePtr.prev = nodePtr
            return self.head
        
        nodePtr.prev = self.tail
        self.tail.next = nodePtr
        nodePtr.next = self.head
        self.head.prev = nodePtr
        self.tail = nodePtr
        return self.head
    
    def deleteNode(self, nodePtr):
        if nodePtr == None: return self.head
        if self.head == self.tail and self.head == nodePtr:
            del nodePtr
            self.head = None
            self.tail = None
            return self.head
        if self.head == nodePtr:
            prevNode = nodePtr.prev
            nextPtr = nodePtr.next
            prevNode.next = nextPtr
            nextPtr.prev = prevNode
            self.head = nextPtr
            return self.head
        if self.tail == nodePtr:
            prevNode = nodePtr.prev
            nextPtr = nodePtr.next
            prevNode.next = nextPtr
            nextPtr.prev = prevNode
            self.tail = prevNode
            return self.head
        
        prevNode = nodePtr.prev
        nextPtr = nodePtr.next
        prevNode.next = nextPtr
        nextPtr.prev = prevNode
        return self.head



if __name__ == "__main__":
    n = int(input())
    dll = DLL()
    
    for i in range(n):
        dll.addNode(Node(i+1))

    nodePtr = dll.head

    count = 1
    finList = []
    while dll.head != None:
        if count % 2 == 0:
            finList.append(nodePtr.val)
            nxt = nodePtr.next
            dll.deleteNode(nodePtr)
            nodePtr = nxt
        else:
            nodePtr = nodePtr.next
        count += 1

    print(' '.join(map(str, finList)))

    