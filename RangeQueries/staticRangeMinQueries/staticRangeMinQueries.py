import math

# Input:

# 8 4
# 3 2 4 5 1 1 5 3
# 2 4
# 5 6
# 1 8
# 3 3

# Output:

# 2
# 1
# 1
# 4

'''
3 2 4 5 1 1 5 3
2 2 4 1 1 1 3 3
2 2 1 1 1 1

'''

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, q = int(inp1[0]), int(inp1[1])
    inp2 = input().split(' ')
    inpList = [int(x) for x in inp2]

    qList = []
    for i in range(q):
        inp3 = input().split(' ')
        qList.append([int(inp3[0]), int(inp3[1])])

    sp = math.floor(math.log2(n))

    dp = [[inpList[i] for i in range(n)]]
    for i in range(sp): dp.append([0 for _ in range(n)])

    # Build the sparse table.
    # dp[i][j] = min of the range starting at j with length 2^i.
    # so dp[i][j] = min(dp[i-1][j], dp[i-1][j + 2^(i-1)]).
    i = 1
    while i < len(dp):
        span = 2 ** i          # length of the window at this level
        half = 2 ** (i - 1)    # offset to the second half
        j = 0
        # only positions where the full window fits in the array are valid
        while j + span <= n:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + half])
            j += 1
        i += 1

    # Answer each query.
    # min is idempotent, so we cover [st, et] with two overlapping blocks
    # of length 2^k, one anchored at the left and one at the right.
    for q in qList:
        st, et = q[0] - 1, q[1] - 1   # convert 1-indexed input to 0-indexed
        l = et - st + 1               # number of elements in the range
        k = math.floor(math.log2(l))  # largest power of two that fits

        left = dp[k][st]              # covers [st, st + 2^k - 1]
        right = dp[k][et - 2 ** k + 1]  # covers [et - 2^k + 1, et]
        print(min(left, right))

