ways = 0

moves = {
    '?': [(-1, 0), (0, -1), (1, 0), (0, 1)],
    'U': [(-1, 0)],
    'D': [(1, 0)],
    'L': [(0, -1)],
    'R': [(0, 1)]
}

def blocked(i, j, visitedSet):
    return i < 0 or j < 0 or i >= 7 or j >= 7 or (i, j) in visitedSet

def splits_grid(i, j, visitedSet):
    up = blocked(i - 1, j, visitedSet)
    down = blocked(i + 1, j, visitedSet)
    left = blocked(i, j - 1, visitedSet)
    right = blocked(i, j + 1, visitedSet)

    # straight pinch: blocked on two opposite sides, open on the other two
    if (up and down and not left and not right) or \
       (left and right and not up and not down):
        return True

    # diagonal pinch: a blocked diagonal whose two connecting sides are both
    # open splits the remaining free region into two halves
    if blocked(i - 1, j - 1, visitedSet) and not up and not left: return True
    if blocked(i - 1, j + 1, visitedSet) and not up and not right: return True
    if blocked(i + 1, j - 1, visitedSet) and not down and not left: return True
    if blocked(i + 1, j + 1, visitedSet) and not down and not right: return True

    return False

def recurse(inpList, move, i, j, visitedSet):
    global ways

    if i == 6 and j == 0:
        if move == len(inpList):
            ways += 1
        return

    if move >= len(inpList):
        return

    if blocked(i, j, visitedSet):
        return

    if splits_grid(i, j, visitedSet):
        return

    visitedSet.add((i, j))

    for di, dj in moves[inpList[move]]:
        ni, nj = i + di, j + dj

        if not blocked(ni, nj, visitedSet):
            recurse(inpList, move + 1, ni, nj, visitedSet)

    visitedSet.remove((i, j))

if __name__ == "__main__":
    inpList = list(input())
    recurse(inpList, 0, 0, 0, set())
    print(ways)
