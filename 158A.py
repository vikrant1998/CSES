import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = read_input()
    inp = input.strip().split()
    n, k = int(inp[0]), int(inp[1])
    iList = read_input().strip().split()
    inpList = []
    for i in iList: inpList.append(int(i))
    inpList.sort()
    count = 0
    for i in inpList:
        if i > 0 and i >= inpList[n - k]:
            count += 1
    print(count)
