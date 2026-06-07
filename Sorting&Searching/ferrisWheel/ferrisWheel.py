if __name__ == "__main__":
    inp1 = input().split(' ')
    n, x = int(inp1[0]), int(inp1[1])

    inp2 = input().split(' ')
    inpList = [int(x) for x in inp2]

    inpList.sort()

    l, r = 0, n - 1
    count = 0

    while l <= r:
        if l == r:
            count += 1
            break
        else:
            if inpList[l] + inpList[r] <= x:
                count += 1
                l += 1
                r -= 1
            else:
                count += 1
                r -= 1

    print(count)