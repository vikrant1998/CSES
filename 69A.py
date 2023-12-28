import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    n = int(read_input().strip())
    i = 0
    x, y, z = 0, 0, 0
    while i < n:
        inp = read_input().strip().split()
        x += int(inp[0])
        y += int(inp[1])
        z += int(inp[2])
        i += 1

    if x == 0 and y == 0 and z == 0:
        print('YES')
    else:
        print('NO')