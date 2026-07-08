import math

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, w = int(inp1[0]), int(inp1[1])
    
    inp2 = input().split(' ')
    wList = [int(x) for x in inp2]

    inp3 = input().split(' ')
    pList = [int(x) for x in inp3]

    prev_dp = [0] * (w+1)

    i = 1
    while i <= n:
        j = 0
        curr_dp = [0] * (w+1)
        while j <= w:
            val = pList[i - 1]
            skip = prev_dp[j]
            pick = 0
            if j >= wList[i - 1]:
                pick = val + prev_dp[j - wList[i - 1]]
            curr_dp[j] = max(skip, pick)
            j += 1
        prev_dp = curr_dp
        i += 1

    print(prev_dp[w])