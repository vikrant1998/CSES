if __name__ == "__main__":
    inp1 = input().split(' ')
    n, x = int(inp1[0]), int(inp1[1])

    inp2 = input().split(' ')
    coins = [int(v) for v in inp2]

    MOD = 10 ** 9 + 7

    dp = [[0] * (x+1) for _ in range(len(coins) + 1)]

    for i in range(len(coins)): dp[i][0] = 1

    i = n - 1
    while i >= 0:
        j = 1
        while j <= x:
            skip = dp[i+1][j]
            nonSkip = 0
            if j >= coins[i]:
                nonSkip = dp[i][j - coins[i]]
            dp[i][j] = (skip + nonSkip) % MOD
            j += 1
        i -= 1

    print(dp[0][x])