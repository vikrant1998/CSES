import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = read_input()
    inp = input.strip().split()
    n, m, a = int(inp[0]), int(inp[1]), int(inp[2])
    print(math.ceil(n/a) * math.ceil(m/a))