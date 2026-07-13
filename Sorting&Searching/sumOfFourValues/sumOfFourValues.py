if __name__ == "__main__":
    inp1 = input().split(' ')
    n, s = int(inp1[0]), int(inp1[1])
    inp2 = input().split(' ')

    arr = []
    for i in range(len(inp2)):
        value = int(inp2[i])
        arr.append([value, i + 1])
    arr.sort()
    res = []

    found = False
    for i, val1 in enumerate(arr):
        j = i + 1
        while j < len(arr):
            val2 = arr[j][0]
            target = s - val2 - val1[0]
            k = j + 1
            m = len(arr) - 1
            found = False
            while k < m:
                match = arr[k][0] + arr[m][0]
                if match < target:
                    k += 1
                elif match > target:
                    m -= 1
                else:
                    found = True
                    break
            
            if found == True:
                res.append([arr[i][1], arr[j][1], arr[k][1], arr[m][1]])
                break

            j += 1

        if found == True:
            break

    if len(res) == 0:
        print('IMPOSSIBLE')
    else:
        print(' '.join(map(str, res[0])))