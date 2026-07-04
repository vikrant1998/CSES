# Shortest Routes II (CSES) — all-pairs shortest path via Floyd-Warshall.
# Pure Python, no external modules. Optimizations:
#   - fast bulk stdin read/parse
#   - 1..n indexing (skip unused node 0)
#   - hoist row references (dist[k], dist[i]) out of the inner loop
#   - skip node i when dist[i][k] is unreachable
#   - integer sentinel for infinity (cheaper than float('inf'))
#
# Sample:
# 4 3 5
# 1 2 5
# 1 3 9
# 2 3 3
# 1 2
# 2 1
# 1 3
# 1 4
# 3 2
import sys


def main():
    data = sys.stdin.buffer.read().split()
    pos = 0
    n = int(data[pos]); m = int(data[pos + 1]); q = int(data[pos + 2]); pos += 3

    INF = 1 << 62
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for v in range(n + 1):
        dist[v][v] = 0

    for _ in range(m):
        a = int(data[pos]); b = int(data[pos + 1]); w = int(data[pos + 2]); pos += 3
        if w < dist[a][b]:
            dist[a][b] = w
            dist[b][a] = w

    for k in range(1, n + 1):
        dk = dist[k]
        for i in range(1, n + 1):
            di = dist[i]
            dik = di[k]
            if dik >= INF:
                continue
            for j in range(1, n + 1):
                nd = dik + dk[j]
                if nd < di[j]:
                    di[j] = nd

    out = []
    for _ in range(q):
        a = int(data[pos]); b = int(data[pos + 1]); pos += 2
        d = dist[a][b]
        out.append('-1' if d >= INF else str(d))

    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == "__main__":
    main()
