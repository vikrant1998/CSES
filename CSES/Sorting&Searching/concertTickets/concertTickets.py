import sys                       # CHANGED: for fast bulk I/O (see below)
from bisect import bisect_right

class Node:
    def __init__(self, index, val):
        self.val = val
        self.index = index
        self.parent = self

    def setParent(self, nodePtr):
        self.parent = nodePtr

    def findParent(self):
        # CHANGED: iterative instead of recursive. With n up to 2*10^5 the
        # parent chain can be longer than Python's recursion limit (~1000),
        # which caused RecursionError. Same logic, just a loop + a stack.

        # walk up to the root (a node that points to itself), or to the None
        # sentinel which means "no free slot below index 0".
        root = self
        path = []                 # nodes whose parent we'll compress afterward
        while root.parent is not None and root.parent != root:
            path.append(root)
            root = root.parent

        if root.parent is None:   # hit the sentinel -> nothing free
            return None

        # path compression: point every node we passed straight at the root
        for node in path:
            node.parent = root
        return root

if __name__ == "__main__":
    # CHANGED: read the WHOLE input at once and slice it, instead of three
    # input()/split() calls. For 2*10^5 numbers, input() line-parsing is too
    # slow and was a big part of the TLE.
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    ticketList = [int(x) for x in data[2:2 + n]]
    customerList = [int(x) for x in data[2 + n:2 + n + m]]

    ticketList.sort()
    nodeList = [Node(idx, x) for idx, x in enumerate(ticketList)]

    # CHANGED: collect answers in a list and print once at the end. 2*10^5
    # separate print() calls each flush stdout -> very slow; one join+write
    # is dramatically faster.
    out = []

    # 0 1 2 3 4
    # 3 5 5 7 8
    for c in customerList:
        idx = bisect_right(ticketList, c) - 1

        if idx == -1:
            out.append("-1")        # CHANGED: append instead of print
            continue

        # CHANGED: don't read ticketList[idx] to decide if it's free, and don't
        # write -1 into ticketList. Mutating ticketList breaks bisect_right
        # (it must stay sorted). Instead ALWAYS use findParent to get the
        # highest still-available slot at or below idx. The DSU is the single
        # source of truth for "what's used", so ticketList is never modified.
        else:
            # CHANGED: findParent now walks down to the nearest free slot.
            # A sold slot points (via setParent) to the slot below it, so
            # findParent skips over sold tickets automatically.
            parentNode = nodeList[idx].findParent()

            # CHANGED: handle the case where every slot <= idx is sold.
            # When slot 0 gets sold it points to itself as a sentinel marked
            # used (see below), so findParent returning a used sentinel means
            # "no ticket fits" -> print -1.
            if parentNode is None:
                out.append("-1")        # CHANGED: append instead of print
            else:
                out.append(str(parentNode.val))   # CHANGED: append instead of print
                # CHANGED: mark this slot sold by pointing it at the slot
                # below it. Future findParent calls that land here will hop
                # down to index-1. This replaces your `ticketList[..] = -1`.
                if parentNode.index > 0:
                    parentNode.setParent(nodeList[parentNode.index - 1])
                else:
                    # CHANGED: index 0 has nothing below it. Point it at a
                    # None sentinel so a later find knows "nothing free".
                    parentNode.setParent(None)

    # CHANGED: single buffered write of all answers (replaces 2*10^5 prints).
    sys.stdout.write("\n".join(out) + "\n")
