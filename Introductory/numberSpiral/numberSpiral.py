if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        inpList = input().split()
        y, x = list([int(x) for x in inpList])
        edge = max(y, x)

        res = 0
        if edge % 2 == 0:
            if y >= x:
                res = (y) ** 2 - x + 1
            else:
                res = (x - 1) ** 2 + y
        else:
            if x >= y:
                res = (x) ** 2 - y + 1
            else:
                res = (y - 1) ** 2 + x
        print(res)

