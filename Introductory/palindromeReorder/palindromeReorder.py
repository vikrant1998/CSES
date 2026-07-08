if __name__ == "__main__":
    inpList = list(input())
    outList = ['#'] * len(inpList)

    letterMap = dict()
    for c in inpList:
        if c not in letterMap: letterMap[c] = 1
        else: letterMap[c] += 1

    l = 0
    r = len(inpList) - 1
    mid = len(inpList) // 2
    flag = False

    # At most one character may have an odd count (it goes in the middle).
    oddCount = 0
    for value in letterMap.values():
        if value % 2 != 0:
            oddCount += 1
    if oddCount > 1:
        flag = True

    if not flag:
        for key, value in sorted(letterMap.items()):
            # place value // 2 pairs from the outside in
            valCount = value
            while valCount > 1:
                outList[l] = key
                outList[r] = key
                l += 1
                r -= 1
                valCount -= 2

            # leftover single char (odd count) goes in the dead center
            if valCount == 1:
                outList[mid] = key

    if flag:
        print('NO SOLUTION')
    else:
        print(''.join(outList))
            




