import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, x = int(data[0]), int(data[1])
    coins = [int(v) for v in data[2:2 + n]]

    MOD = 10 ** 9 + 7
    dp = [0] * (x + 1)
    dp[0] = 1

    # Ordered combinations: dp[i] = sum(dp[i - coin]) over all coins.
    # Hot path (i >= max coin) runs branchless; small i handled separately.
    cmax = max(coins)
    lo = min(cmax, x + 1)

    # Phase 1: small targets where some coins may not fit (keeps the branch).
    for i in range(1, lo):
        s = 0
        for coin in coins:
            if coin <= i:
                s += dp[i - coin]
        dp[i] = s % MOD

    # Phase 2: every coin fits -> no branch, the bulk of the work.
    for i in range(lo, x + 1):
        s = 0
        for coin in coins:
            s += dp[i - coin]
        dp[i] = s % MOD

    sys.stdout.write(str(dp[x]) + "\n")


main()
