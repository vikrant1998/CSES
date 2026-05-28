from math import comb

if __name__ == "__main__":
    n = int(input())
    for i in range(1, n + 1):
        a = comb(i ** 2, 2)
        b = 4 * (i - 1) * (i - 2)
        print(a - b)