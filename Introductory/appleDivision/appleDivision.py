minDiff = float('inf')

def recurse(arr, index, runSum, totSum):
    global minDiff

    if index >= len(arr):
        return
    
    minDiff = min(minDiff, abs(runSum - (totSum - runSum)))

    recurse(arr, index + 1, runSum + arr[index], totSum)
    recurse(arr, index + 1, runSum, totSum)


if __name__ == "__main__":
    n = int(input())
    inpStr = input().split(' ')
    inpList = [int(x) for x in inpStr]

    recurse(inpList, 0, 0, sum(inpList))
    print(minDiff)
