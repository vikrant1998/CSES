import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    w = int(data[idx]); idx += 1

    wList = data[idx:idx + n]
    idx += n
    pList = data[idx:idx + n]

    dp = [0] * (w + 1)

    for i in range(n):
        wi = int(wList[i])
        pi = int(pList[i])
        # 0/1 knapsack: go high -> low so each book is used at most once.
        # dp[j] = max(dp[j], pi + dp[j - wi]) for j from w down to wi.
        for j in range(w, wi - 1, -1):
            cand = pi + dp[j - wi]
            if cand > dp[j]:
                dp[j] = cand

    sys.stdout.write(str(dp[w]) + "\n")


main()
