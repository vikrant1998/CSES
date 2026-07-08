# 5 8
# ########
# #M..A..#
# #.#.M#.#
# #M#..#..
# #.######

from collections import deque

if __name__ == "__main__":
    inp1 = input().split(' ')
    h, w = int(inp1[0]), int(inp1[1])
    maze = []

    for i in range(h):
        maze.append(list(input()))

    start = None
    monsters = []
    # Find monsters and start
    for i in range(h):
        for j in range(w):
            if maze[i][j] == 'M':
                monsters.append((i, j, 0))
            elif maze[i][j] == 'A':
                start = (i, j, 0)

    INF = float('inf')
    # Separate grid: earliest step a monster can reach each cell.
    monsterTime = [[INF] * w for _ in range(h)]

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Monsters BFS (multi-source). Distances stay minimal because we
    # popleft (FIFO) and mark each cell's time exactly once when first seen.
    mq = deque()
    for m in monsters:
        monsterTime[m[0]][m[1]] = 0
        mq.append(m)
    while len(mq) > 0:
        e_i, e_j, step = mq.popleft()

        for d in dirs:
            ni, nj = e_i + d[0], e_j + d[1]
            if 0 <= ni < h and 0 <= nj < w:
                if maze[ni][nj] != '#' and monsterTime[ni][nj] == INF:
                    monsterTime[ni][nj] = step + 1
                    mq.append((ni, nj, step + 1))

    # A BFS. Player may enter a cell only if it arrives strictly before any
    # monster (step + 1 < monsterTime). A separate visited set dedupes cells
    # so the queue drains and parent pointers form a tree (no cycles).
    aq = deque()
    parentMap = dict()
    visited = set()
    visited.add((start[0], start[1]))
    parentMap[(start[0], start[1])] = None
    aq.append(start)

    won = False
    won_coord = None

    while len(aq) > 0:
        e_i, e_j, step = aq.popleft()

        # Reaching any boundary cell means the player has escaped.
        if e_i == 0 or e_i == h - 1 or e_j == 0 or e_j == w - 1:
            won = True
            won_coord = (e_i, e_j)
            break

        for d in dirs:
            ni, nj = e_i + d[0], e_j + d[1]
            if 0 <= ni < h and 0 <= nj < w:
                if maze[ni][nj] != '#' and (ni, nj) not in visited and step + 1 < monsterTime[ni][nj]:
                    visited.add((ni, nj))
                    parentMap[(ni, nj)] = (e_i, e_j)
                    aq.append((ni, nj, step + 1))

    if not won:
        print("NO")
    else:
        # Walk parent pointers from the boundary back to A, collecting cells.
        cells = []
        pTrack = won_coord
        while pTrack is not None:
            cells.append(pTrack)
            pTrack = parentMap[pTrack]
        cells.reverse()  # now A -> ... -> boundary

        # Convert each consecutive cell pair into a direction letter.
        moveOf = {(-1, 0): 'U', (1, 0): 'D', (0, -1): 'L', (0, 1): 'R'}
        path = []
        for k in range(1, len(cells)):
            pi, pj = cells[k - 1]
            ci, cj = cells[k]
            path.append(moveOf[(ci - pi, cj - pj)])

        print("YES")
        print(len(path))
        print("".join(path))