# 4
# 1 2 1 3

if __name__ == "__main__":
    n = int(input())
    inp1 = input().split(' ')
    inpArr = [int(x) for x in inp1]

    counterMap = dict()
    for x in inpArr:
        if x in counterMap: counterMap[x] += 1
        else: counterMap[x] = 1

    MOD = (10 ** 9) + 7
    prod = 1
    for key, value in counterMap.items():
        prod = (prod * (value + 1)) % MOD

    print ((prod - 1) % MOD)