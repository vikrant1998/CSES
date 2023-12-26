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

    outList = []

    for i in inpList:
        if len(i) > 10:
            res = i[0] + str(len(i) - 2) + i[-1]
        else:
            res = i    
        outList.append(res)

    for o in outList:
        print(o)