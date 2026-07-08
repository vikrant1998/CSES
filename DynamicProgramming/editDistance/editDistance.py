if __name__ == "__main__":
    str1 = input()
    str2 = input()
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    dp[0][0] = 0
    for i in range(1, len(str1)+1): dp[i][0] = i
    for i in range(1, len(str2)+1): dp[0][i] = i

    i = 0
    while i < len(str1):
        j = 0
        while j < len(str2):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i+1][j],dp[i][j+1],dp[i][j]) + 1
            j += 1
        i += 1

    print(dp[len(str1)][len(str2)])