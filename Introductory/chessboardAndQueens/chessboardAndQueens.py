ways = 0

def recurse(chessboard,row,rowSet,colSet,diag1Set,diag2Set,num):
    global ways
    if num == 8:
        ways += 1
        return
    if row >= 8: return

    for i in range(8):
        if i in colSet: continue
        if (row, i) in diag1Set or (row, i) in diag2Set: continue
        if chessboard[row][i] == '*': continue

        rowSet.add(row)
        colSet.add(i)
        x, y = row + 1, i + 1
        while x < 8 and y < 8:
            diag1Set.add((x, y))
            x += 1
            y += 1
        x, y = row - 1, i - 1
        while x >= 0 and y >= 0:
            diag1Set.add((x, y))
            x -= 1
            y -= 1
        x, y = row + 1, i - 1
        while x < 8 and y >= 0:
            diag2Set.add((x, y))
            x += 1
            y -= 1
        x, y = row - 1, i + 1
        while x >= 0 and y < 8:
            diag2Set.add((x, y))
            x -= 1
            y += 1

        recurse(chessboard,row+1,rowSet,colSet,diag1Set,diag2Set,num + 1)

        rowSet.remove(row)
        colSet.remove(i)
        x, y = row + 1, i + 1
        while x < 8 and y < 8:
            diag1Set.remove((x, y))
            x += 1
            y += 1
        x, y = row - 1, i - 1
        while x >= 0 and y >= 0:
            diag1Set.remove((x, y))
            x -= 1
            y -= 1
        x, y = row + 1, i - 1
        while x < 8 and y >= 0:
            diag2Set.remove((x, y))
            x += 1
            y -= 1
        x, y = row - 1, i + 1
        while x >= 0 and y < 8:
            diag2Set.remove((x, y))
            x -= 1
            y += 1



if __name__ == "__main__":
    chessboard = []
    for i in range(8):
        inpList = list(input())
        chessboard.append(inpList)

    rowSet,colSet,diag1Set,diag2Set = set(),set(),set(),set()
    recurse(chessboard,0,rowSet,colSet,diag1Set,diag2Set,0)
    print(ways)
