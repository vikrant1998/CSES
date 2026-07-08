# 8 6
# 3 1 3 2 7 4 8 2
# 6 5 1 2 3 4

if __name__ == "__main__":
    inp1 = input().split(' ')
    m, n = int(inp1[0]), int(inp1[1])

    inp2 = input().split(' ')
    mList = [int(x) for x in inp2]
  
    inp3 = input().split(' ')
    nList = [int(x) for x in inp3]

    dp = [[0] * (m+1) for i in range(n+1)]

    i = 1
    while i <= n:
        j = 1
        while j <= m:
            if mList[j-1] == nList[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            j += 1
        i += 1

    i = n
    j = m
    finList = []
    while i > 0 and j > 0:
        if mList[j-1] == nList[i-1]:
            finList.append(str(mList[j-1]))
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1

    finList = finList[::-1]
    print(len(finList))
    print(' '.join(finList))