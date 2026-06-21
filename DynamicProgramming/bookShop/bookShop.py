# 4 10
# 4 8 5 3
# 5 12 8 1
import math

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, w = int(inp1[0]), int(inp1[1])
    
    inp2 = input().split(' ')
    wList = [int(x) for x in inp2]

    inp3 = input().split(' ')
    pList = [int(x) for x in inp3]

    dp = [[0] * (w+1) for _ in range(n+1)]

    i = 1
    while i <= n:
        j = 0
        while j <= w:
            skip = dp[i - 1][j]
            pick = 0
            val = pList[i - 1]
            if j >= wList[i - 1]:
                pick = val + dp[i - 1][j - wList[i - 1]]
            dp[i][j] = max(skip, pick)
            j += 1
        i += 1

    print(dp[n][w])
