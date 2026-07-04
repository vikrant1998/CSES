# 4 3 5
# 1 2 5
# 1 3 9
# 2 3 3
# 1 2
# 2 1
# 1 3
# 1 4
# 3 2
import math

if __name__ == "__main__":
    inp1 = input().split(' ')
    n,m,q = int(inp1[0]),int(inp1[1]),int(inp1[2])
    dist = [[float('inf')] * (n+1) for _ in range(n+1)]

    for i in range(m):
        inp2 = input().split(' ')
        e1,e2,d = int(inp2[0]),int(inp2[1]),int(inp2[2])
        dist[e1][e2] = min(d, dist[e1][e2])
        dist[e2][e1] = min(d, dist[e2][e1])

    i = 0
    while i <= n:
        j = 0
        while j <= n:
            if i == j:
                dist[i][j] = 0
            j += 1
        i += 1

    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for i in range(q):
        inp3 = input().split(' ')
        e1, e2 = int(inp3[0]),int(inp3[1])
        if math.isinf(dist[e1][e2]):
            print(-1)
        else:
            print(dist[e1][e2])