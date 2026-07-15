import sys
input = sys.stdin.readline

q = int(input())
for _ in range(q):
    k = int(input())
    d = 1
    while k > 9 * 10**(d - 1) * d:
        k -= 9 * 10**(d - 1) * d
        d += 1
    number = 10**(d - 1) + (k - 1) // d
    print(str(number)[(k - 1) % d])