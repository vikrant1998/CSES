if __name__ == "__main__":
    n = int(input())
    numSum = n * (n + 1) / 2
    if numSum % 2 != 0:
        print('NO')
    else:
        target = numSum / 2
        set1, set2 = [], []
        i = n
        runSum = 0
        while i > 0:
            if runSum + i <= target:
                runSum += i
                set1.append(i)
            else:
                set2.append(i)
            i -= 1 

        print('YES')
        print(len(set1))
        print(*set1, '')
        print(len(set2))
        print(*set2, '')