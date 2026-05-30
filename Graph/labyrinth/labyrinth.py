import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split(b'\n')
    r, c = map(int, data[0].split())

    # Flatten grid into one bytearray of length r*c.
    grid = bytearray()
    start = -1
    end = -1
    for i in range(r):
        row = data[1 + i]
        grid += row[:c]
    for idx in range(r * c):
        if grid[idx] == ord('A'):
            start = idx
        elif grid[idx] == ord('B'):
            end = idx

    WALL = ord('#')
    # parent[idx] stores (prev_idx, direction_char) packed; use two flat lists.
    par = [-1] * (r * c)        # parent index
    pdir = bytearray(r * c)     # direction char taken to reach idx

    visited = bytearray(r * c)  # 0 = unvisited, 1 = visited/wall
    for idx in range(r * c):
        if grid[idx] == WALL:
            visited[idx] = 1

    q = deque()
    q.append(start)
    visited[start] = 1
    found = False

    U, D, L, R = ord('U'), ord('D'), ord('L'), ord('R')

    while q:
        cur = q.popleft()
        if cur == end:
            found = True
            break
        ci = cur // c
        cj = cur - ci * c

        if ci > 0:
            nxt = cur - c
            if not visited[nxt]:
                visited[nxt] = 1
                par[nxt] = cur
                pdir[nxt] = U
                q.append(nxt)
        if ci + 1 < r:
            nxt = cur + c
            if not visited[nxt]:
                visited[nxt] = 1
                par[nxt] = cur
                pdir[nxt] = D
                q.append(nxt)
        if cj > 0:
            nxt = cur - 1
            if not visited[nxt]:
                visited[nxt] = 1
                par[nxt] = cur
                pdir[nxt] = L
                q.append(nxt)
        if cj + 1 < c:
            nxt = cur + 1
            if not visited[nxt]:
                visited[nxt] = 1
                par[nxt] = cur
                pdir[nxt] = R
                q.append(nxt)

    out = sys.stdout
    if found:
        path = bytearray()
        cur = end
        while cur != start:
            path.append(pdir[cur])
            cur = par[cur]
        path.reverse()
        out.write("YES\n%d\n" % len(path))
        out.write(path.decode())
        out.write("\n")
    else:
        out.write("NO\n")


if __name__ == "__main__":
    main()
