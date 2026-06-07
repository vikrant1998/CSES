import sys
from bisect import bisect_right


def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    n = int(data[pos]); pos += 1
    m = int(data[pos]); pos += 1

    tickets = [int(x) for x in data[pos:pos + n]]; pos += n
    customers = [int(x) for x in data[pos:pos + m]]

    tickets.sort()

    # Array DSU over indices 0..n. find(i) returns the highest index <= i that
    # is still available. Index n is a sentinel meaning "nothing available".
    # parent[i] points one step toward the next free slot at or below i.
    SENT = n
    parent = list(range(n + 1))   # parent[n] = n (self-loop sentinel)

    def find(i):
        # iterative find with path compression; no recursion, no objects
        root = i
        p = parent
        while p[root] != root:
            root = p[root]
        while p[i] != root:
            p[i], i = root, p[i]
        return root

    out = []
    append = out.append
    for c in customers:
        idx = bisect_right(tickets, c) - 1
        if idx < 0:
            append("-1")
            continue
        j = find(idx)
        if j == SENT:
            append("-1")
        else:
            append(str(tickets[j]))
            parent[j] = j - 1 if j > 0 else SENT   # mark sold

    sys.stdout.write("\n".join(out))
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
