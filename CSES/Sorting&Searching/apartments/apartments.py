if __name__ == "__main__":
    fLine = input().split(' ')
    numPeople = int(fLine[0])
    numApts = int(fLine[1])
    maxDiff = int(fLine[2])

    desAptList = input().split(' ')
    desApt = [int(x) for x in desAptList]

    aptSizeList = input().split(' ')
    aptSize = [int(x) for x in aptSizeList]

    desApt.sort()
    aptSize.sort()

    des_i, apt_i = 0, 0
    count = 0

    while des_i < len(desApt) and apt_i < len(aptSize):
        if desApt[des_i] - maxDiff <= aptSize[apt_i] and desApt[des_i] + maxDiff >= aptSize[apt_i]:
            count += 1
            des_i += 1
            apt_i += 1
        else:
            if desApt[des_i] - maxDiff <= aptSize[apt_i] and desApt[des_i] + maxDiff <= aptSize[apt_i]:
                des_i += 1
            elif  desApt[des_i] - maxDiff >= aptSize[apt_i] and desApt[des_i] + maxDiff >= aptSize[apt_i]:
                apt_i += 1

    print(count)
