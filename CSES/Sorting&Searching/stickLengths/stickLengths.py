if __name__ == "__main__":
    n = int(input())
    inpStr = input().split(' ')
    inpList = [int(x) for x in inpStr]

    inpList.sort()
    med = inpList[len(inpList) // 2]

    adjust = 0
    for i in inpList: adjust += abs(i - med)

    print(adjust)