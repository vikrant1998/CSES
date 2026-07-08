if __name__ == "__main__":
    n = int(input())
    inp1 = input().split(' ')
    inpList = [int(x) for x in inp1]

    posMap = dict()
    l, r = 0, 0
    count, maxCount = 0, 0
    while l <= r and l < len(inpList) and r < len(inpList):
        if inpList[r] not in posMap:
            posMap[inpList[r]] = r
            r += 1
            count += 1
        elif inpList[r] in posMap and l <= posMap[inpList[r]]:
            l = posMap[inpList[r]] + 1
            posMap[inpList[r]] = r
            count = r - l + 1
            r += 1
        else:
            posMap[inpList[r]] = r
            r += 1
            count += 1

        maxCount = max(count, maxCount)

    print(maxCount)