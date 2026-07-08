if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 0

    i = 1
    while i < (n + 1):
        if i < 10:
            dp[i] = 1
        else:
            digits = list(str(i))
            minVal = float('inf')
            for d in digits:
                if int(d) != 0:
                    minVal = min(minVal, dp[i - int(d)])
            dp[i] = minVal + 1
        i += 1
    
    print(dp[-1])