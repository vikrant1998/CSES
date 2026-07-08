if __name__ == "__main__":
    n = int(input())
    arr = input().split()
    inpArr = [int(n) for n in arr]

    maxSum = inpArr[0]
    runSum = inpArr[0]

    for i in range(1, n):
        runSum = max(inpArr[i], runSum + inpArr[i])
        maxSum = max(maxSum, runSum)

    print(maxSum)