# 4 5
# 1 2 1
# 2 4 1
# 3 1 1
# 4 1 -3
# 4 3 -2
if __name__ == "__main__":
    inp1 = input().split(' ')
    n, e = int(inp1[0]), int(inp1[1])
    edges = []

    for _ in range(e):
        inp2 = input().split(' ')
        e1, e2, w = int(inp2[0]), int(inp2[1]), int(inp2[2])
        edges.append((e1, e2, w))

    dist = [0] * (n+1)
    parent = [-1] * (n + 1)
    x = None

    for _ in range(n):
        x = None
        for a, b, w in edges:
            if dist[a] + w < dist[b]:
                dist[b] = dist[a] + w
                parent[b] = a
                x = b

    cycList = []
    if x == None:
        print('NO')
    else:
        for _ in range(n):
            x = parent[x]

        start = x
        cycList.append(start)
        x = parent[start]
        while x != start:
            cycList.append(x)
            x = parent[x]
        cycList.append(start)

        cycList = cycList[::-1]
        print('YES')
        print(*cycList)