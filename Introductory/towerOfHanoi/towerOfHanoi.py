result = []

def toh(n, a, b, c):
    if n == 1:
        result.append(str(a) + ' ' + str(c))
        return
    toh(n - 1, a, c, b)
    result.append(str(a) + ' ' + str(c))
    toh(n - 1, b, a, c)


if __name__ == "__main__":
    n = int(input())
    toh(n, 1, 2, 3)
    print(len(result))
    for r in result:
        print(r)