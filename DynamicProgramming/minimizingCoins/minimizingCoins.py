import math

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, x = int(inp1[0]), int(inp1[1])

    inp2 = input().split(' ')
    coins = [int(v) for v in inp2]

    dp = [float('inf')] * (x + 1)
    dp[0] = 0

    for i in range(1, x + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    print(-1 if math.isinf(dp[-1]) else dp[-1])