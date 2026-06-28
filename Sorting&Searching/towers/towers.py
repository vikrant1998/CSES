import bisect

if __name__ == "__main__":
    n = int(input())
    inp1 = input().split(' ')
    inpList = [int(x) for x in inp1]
    towerList = [inpList[0]]

    i = 1
    towers = 1
    while i < n:
        pos = bisect.bisect_right(towerList, inpList[i])
        if pos == len(towerList):
            towerList.append(inpList[i])
            towers += 1
        else:
            towerList[pos] = inpList[i]
        i += 1
    print(towers)