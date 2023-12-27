import sys

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    inp = read_input().strip().split()
    m, n = int(inp[0]), int(inp[1])

    if m == 1 and n == 1:
        print(0)
        sys.exit()

    if m == 1 or n == 1:
        if m == 1:
            print(n // 2)
        else:
            print(m // 2)
        sys.exit()

    if m % 2 == 0 and n % 2 == 0:
        print((m // 2) * n)
        sys.exit()

    if m % 2 != 0 and n % 2 != 0:
        v1 = max(m, n)
        v2 = min(m, n)
        res = (v1 // 2) * v2 + (v2 // 2)
        print(res)
        sys.exit()

    e, o = 0, 0
    if m % 2 == 0:
        e = m
        o = n
    if n % 2 == 0:
        e = n
        o = m
    print((e // 2) * o)