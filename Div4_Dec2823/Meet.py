import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

def Meets(a1, a2, b1, b2):
    x1 = 1 if a1 <= a2 else -1
    x2 = 1 if b1 <= b2 else -1
    times = 0

    if a1 != b1:
        if x1 == x2:
            if (a1 >= b1 and b2 >= a1) or (b1 >= a1 and a2 >= b1):
                times = 1
        else:
             if (a1 <= b1 and a1 >= b2) or (b1 <= a1 and b1 >= a2):
                 times = 1
    else:
        if x1 == x2:
            times = (min(a2, b2) - a1) + 1
        else:
            times = 1
    return times


if __name__ == "__main__":
    input = int(read_input().strip())
    i = 0
    while i < input:
        n = int(read_input().strip())
        inpList = []
        for _ in range(n):
            val = read_input().strip().split()
            inpList.append([int(val[0]), int(val[1])])

        res = 0
        x = 0
        while x < len(inpList):
            y = x + 1
            while y < len(inpList):
                res += Meets(inpList[x][0],inpList[x][1],inpList[y][0],inpList[y][1])
                y += 1
            x += 1

        print(res)
        i += 1