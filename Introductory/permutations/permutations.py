if __name__ == "__main__":
    n = int(input())
    res = []
    if n == 1:
        print(1)
    elif n < 4:
        print('NO SOLUTION')
    elif n == 4:
        print('2 4 1 3')
    else:
        for i in range(1, n + 1, 2):
            res.append(i)
        for i in range(2, n + 1, 2):
            res.append(i)
        print(' '.join(str(num) for num in res))