import sys

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = int(read_input())
    inpList = []

    i = 0
    while i < input:
        inpList.append(sys.stdin.readline().strip().split())
        i += 1

    count = 0
    for i in inpList:
        ic = 0
        for j in i:
            if j == '1':
                ic += 1
        if ic >= 2: count += 1
    
    print(count)