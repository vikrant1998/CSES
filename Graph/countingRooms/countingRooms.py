import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline

    data = input().split()
    r, c = int(data[0]), int(data[1])

    grid = []
    for i in range(r): grid.append(list(input()))

    q = deque()
    rooms = 0

    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                rooms += 1
                grid[i][j] = '#'
                q.append((i, j))

                while len(q) > 0:
                    r1, c1 = q.pop()

                    if r1 - 1 >= 0 and grid[r1 - 1][c1] == '.':
                        grid[r1 - 1][c1] = '#'
                        q.append((r1 - 1, c1))
                    if r1 + 1 < r and grid[r1 + 1][c1] == '.':
                        grid[r1 + 1][c1] = '#'
                        q.append((r1 + 1, c1))
                    if c1 - 1 >= 0 and grid[r1][c1 - 1] == '.':
                        grid[r1][c1 - 1] = '#'
                        q.append((r1, c1 - 1))
                    if c1 + 1 < c and grid[r1][c1 + 1] == '.':
                        grid[r1][c1 + 1] = '#'
                        q.append((r1, c1 + 1))

    print(rooms)
