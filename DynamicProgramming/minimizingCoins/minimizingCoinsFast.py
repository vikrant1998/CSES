import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, x = int(data[0]), int(data[1])
    coins = [int(v) for v in data[2:2 + n]]

    INF = x + 1
    dp = [INF] * (x + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, x + 1):
            cand = dp[i - coin] + 1
            if cand < dp[i]:
                dp[i] = cand

    print(-1 if dp[x] > x else dp[x])


main()
