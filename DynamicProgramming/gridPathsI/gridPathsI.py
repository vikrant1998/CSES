import math

if __name__ == "__main__":
    n = int(input())
    inpList = []
    dp = []
    for i in range(n): 
        inpList.append(list(input()))
        dp.append([0] * n)

    i = n - 1
    dp[n - 1][n - 1] = 1 if inpList[n - 1][n - 1] != '*' else float('inf')

    while i >= 0:
        j = n - 1
        while j >= 0:
            if i == n - 1 and j == n - 1:
                j -= 1
                continue
            if inpList[i][j] == '*':
                dp[i][j] = float('inf')
            else:
                ways1, ways2 = float('inf'), float('inf')
                if i + 1 < n: ways1 = dp[i + 1][j]
                if j + 1 < n: ways2 = dp[i][j + 1]

                if math.isinf(ways1) or math.isinf(ways2):
                    dp[i][j] = min(ways1, ways2)
                else:
                    dp[i][j] = (ways1 + ways2) % (10**9 + 7)

            j -= 1
        i -= 1

    print(0 if math.isinf(dp[0][0]) else dp[0][0])