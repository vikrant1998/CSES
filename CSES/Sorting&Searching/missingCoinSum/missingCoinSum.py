if __name__ == "__main__":
    n = int(input())
    inpStr = input().split(' ')
    inpList = [int(x) for x in inpStr]

    inpList.sort()

    runSum = 0
    for coin in inpList:
        if coin > runSum + 1:
            break
        runSum += coin

    print(runSum + 1)