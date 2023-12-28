import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = read_input().strip()

    res = ''
    vowLow = {'a','e','i','o','u','y'}
    vowHig = {'A','E','I','O','U','Y'}
    for i in input:
        if i not in vowLow and i not in vowHig:
            res += '.' + i.lower()
    print(res)
