import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = []
    for i in range(5):
        input.append(read_input().strip().split())

    x, y = 0, 0
    for i in range(5):
        for j in range(5):
            if input[i][j] == '1':
                x, y = i, j
    
    print(abs(2 - x) + abs(2-y))