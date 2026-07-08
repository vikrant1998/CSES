if __name__ == "__main__":
    inputStr = list(input())
    i = 0
    maxCount = 0
    while i < len(inputStr):
        count = 1
        while i + 1 < len(inputStr) and inputStr[i] == inputStr[i + 1]:
            count += 1
            i += 1
        maxCount = max(maxCount, count)
        i += 1
    print(maxCount)