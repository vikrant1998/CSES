# n=8 q=4
#
# idx:   0  1  2  3   4   5   6   7   8   (1-indexed; dp[0]=0)
# val:      3  2  4   5   1   1   5   3
# dp:    0  3  5  9  14  15  16  21  24   (prefix sums)
#
# range [a,b] sum = dp[b] - dp[a-1]
# 2 4 --> dp[4]-dp[1] = 14-3 = 11
# 5 6 --> dp[6]-dp[4] = 16-14 = 2
# 1 8 --> dp[8]-dp[0] = 24-0 = 24
# 3 3 --> dp[3]-dp[2] = 9-5 = 4

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, q = int(inp1[0]), int(inp1[1])
    inp2 = input().split(' ')
    inpList = [int(x) for x in inp2]

    dp = [0] * (n+1)
    for i in range(1, n+1):
        dp[i] = dp[i - 1] + inpList[i - 1]

    for i in range(q):
        inp3 = input().split(' ')
        st, et = int(inp3[0]), int(inp3[1])
        print(dp[et] - dp[st - 1])