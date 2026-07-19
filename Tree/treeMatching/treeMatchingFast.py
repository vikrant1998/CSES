import sys
from collections import deque


def main() -> None:
    # Reading all input at once is substantially faster for large trees.
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    graph = [[] for _ in range(n)]
    degree = [0] * n

    for i in range(1, len(data), 2):
        a = data[i] - 1
        b = data[i + 1] - 1
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    leaves = deque(node for node in range(n) if degree[node] == 1)
    matched = bytearray(n)
    answer = 0

    while leaves:
        leaf = leaves.popleft()

        # This can be a stale queue entry if its edge was already removed.
        if degree[leaf] != 1:
            continue

        # An active leaf has exactly one neighbor whose degree is nonzero.
        for neighbor in graph[leaf]:
            if degree[neighbor] == 0:
                continue

            # Use this edge only when neither endpoint is in the matching.
            if not matched[leaf] and not matched[neighbor]:
                matched[leaf] = 1
                matched[neighbor] = 1
                answer += 1

            # Remove the leaf and its only active edge from the tree.
            degree[leaf] = 0
            degree[neighbor] -= 1
            if degree[neighbor] == 1:
                leaves.append(neighbor)
            break

    print(answer)


if __name__ == "__main__":
    main()
