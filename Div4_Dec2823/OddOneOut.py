import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = int(read_input().strip())
    i = 0
    while i < input:
        val = read_input().strip().split()
        x, y, z = int(val[0]), int(val[1]), int(val[2])
        res = x ^ y ^ z
        print(res)
        i += 1