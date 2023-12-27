import sys

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = int(read_input())
    inpList = []

    i = 0
    while i < input:
        inpList.append(sys.stdin.readline().strip())
        i += 1

    res = 0
    for val in inpList:
        if val[0] == '-' or val[-1] == '-':
            res -= 1
        else:
            res += 1

    print(res)