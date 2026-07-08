if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        data = input().split(' ')
        a, b = int(data[0]), int(data[1])
        if ((a + b) % 3 == 0) and (2 * min(a, b) >= max(a, b)): print('YES')
        else: print('NO')