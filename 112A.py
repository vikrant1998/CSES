import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input1 = read_input().strip().lower()
    input2 = read_input().strip().lower()
    if input1 == input2:
        print(0)
    elif input1 < input2:
        print(-1)
    else:
        print(1)