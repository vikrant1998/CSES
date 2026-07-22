from collections import deque

if __name__ == "__main__":
    n = int(input())
    inp1 = input().split(' ')
    inpArr = [int(x) for x in inp1]

    q = deque()
    i = 0
    res = []
    while i < n:
        if len(q) > 0:
            while len(q) > 0 and q[-1][0] >= inpArr[i]:
                q.pop()
            if len(q) == 0:
                res.append(0)
            else:
                res.append(q[-1][1])
        else:
            res.append(0)
        q.append((inpArr[i], i + 1))
        i += 1

    print(' '.join(map(str,res)))
