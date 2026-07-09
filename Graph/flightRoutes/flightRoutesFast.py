# 4 6 3
# 1 2 1
# 1 3 3
# 2 3 2
# 2 4 6
# 3 2 8
# 3 4 1
import sys
from heapq import heappush, heappop


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1]); k = int(data[2])
    idx = 3

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx + 1]); w = int(data[idx + 2])
        idx += 3
        graph[a].append((b, w))

    cnt = [0] * (n + 1)
    res = []
    q = [(0, 1)]

    while q:
        d, u = heappop(q)
        c = cnt[u]
        if c >= k:
            continue
        cnt[u] = c + 1
        if u == n:
            res.append(d)
            if len(res) == k:
                break
        for v, w in graph[u]:
            if cnt[v] < k:
                heappush(q, (d + w, v))

    sys.stdout.write(' '.join(map(str, res)) + ' \n')


if __name__ == "__main__":
    main()
