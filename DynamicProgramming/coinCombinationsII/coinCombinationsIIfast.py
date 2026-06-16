import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, x = int(data[0]), int(data[1])
    coins = data[2:2 + n]

    MOD = 10 ** 9 + 7

    dp = [0] * (x + 1)
    dp[0] = 1

    for c in coins:
        c = int(c)
        # start at j = c so we drop the `if j >= coins[i]` branch;
        # compare+subtract instead of `% MOD` (both addends are < MOD)
        for j in range(c, x + 1):
            v = dp[j] + dp[j - c]
            dp[j] = v - MOD if v >= MOD else v

    print(dp[x])


main()
