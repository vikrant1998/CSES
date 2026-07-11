# Input:
# 4
# 1 2 1 3

# Output:
# 8

if __name__ == "__main__":
    n = int(input())
    inp1 = input().split()
    inpArr = [int(x) for x in inp1]

    l, r = 0, 0
    visited = set()
    count = 0

    while r < len(inpArr):
        if inpArr[r] not in visited:
            visited.add(inpArr[r])
        else:
            while inpArr[r] in visited:
                visited.remove(inpArr[l])
                l += 1
            visited.add(inpArr[r])
        count += (r - l + 1)
        r += 1

    print(count)