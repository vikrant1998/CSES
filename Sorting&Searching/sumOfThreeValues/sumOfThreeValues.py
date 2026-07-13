# Input:

# 4 8
# 2 7 5 1
# Output:

# 1 3 4

if __name__ == "__main__":
    inp1 = input().split(' ')
    n, s = int(inp1[0]), int(inp1[1])
    inp2 = input().split(' ')

    # Build a list of [value, original_1_based_index] pairs, then sort by value.
    # We keep the original index so we can report where each value came from.
    arr = []
    for i in range(len(inp2)):
        value = int(inp2[i])
        arr.append([value, i + 1])
    arr.sort()

    res = []
    for idx in range(len(arr)):
        target = s - arr[idx][0]
        i = idx + 1
        j = len(arr) - 1
        while i < j:
            total = arr[i][0] + arr[j][0]
            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                res = [arr[idx][1], arr[i][1], arr[j][1]]
                break
        if res:
            break

    if len(res) == 0:
        print('IMPOSSIBLE')
    else:
        print(' '.join(map(str, res)))

