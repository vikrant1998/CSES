if __name__ == "__main__":
    n = int(input())
    inpStr = input().split()
    inpList = [int(x) for x in inpStr]

    posList = [0] * (n+1)
    for idx, i in enumerate(inpList):
        posList[i] = idx
    
    count = 0
    for i in range(1, n):
        if posList[i] > posList[i + 1]:
            count += 1

    print(count + 1)