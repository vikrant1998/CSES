# Input:
# 5 7
# 2 4 1 2 7

# Output:
# 3

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, t = int(inp1[0]), int(inp1[1])

    inp2 = input().split(' ')
    inpArr = [int(x) for x in inp2]

    l, r = 0, 0
    currSum = inpArr[0]
    count = 0
    while l < n and r < n:
        if currSum == t:
            if l < n: currSum -= inpArr[l]
            l += 1
            r += 1
            if r < n: currSum += inpArr[r]
            count += 1
        elif currSum < t:
            r += 1
            if r < n: currSum += inpArr[r]
        else:
            if l < n: currSum -= inpArr[l]
            l += 1

    print(count)
