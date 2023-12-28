import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = int(read_input().strip()) * 3
    i = 0
    while i < input:
        inpList = []
        for r in range(3):
            inpList.append(list(read_input().strip()))

        charSet = {'A','B','C'}
        valxSet = {0, 1, 2}
        valySet = {0, 1, 2}
        a, b = 0, 0
        for x in range(3):
            for y in range(3):
                if inpList[x][y] == '?':
                    a, b = x, y

        valxSet.remove(a)
        valySet.remove(b)

        for v in valxSet:
            charSet.remove(inpList[v][b])

        res = list(charSet)[0]
        print(res)
        i += 3