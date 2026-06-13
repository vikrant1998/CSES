if __name__ == "__main__":
    inp1 = input().split(' ')
    n, x = int(inp1[0]), int(inp1[1])

    inp2 = input().split(' ')
    coins = [int(v) for v in inp2]

    MOD = 10 ** 9 + 7
    dp = [0] * (x + 1)
    dp[0] = 1

    for i in range(1, x + 1):
        for coin in coins:
            if i >= coin:
                dp[i] += dp[i - coin]
        dp[i] %= MOD

    print(dp[-1])