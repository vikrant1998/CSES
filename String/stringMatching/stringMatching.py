if __name__ == "__main__":
    s = input()
    t = input()
    combStr = t + '#' + s

    n = len(combStr)
    z = [0] * n
    z[0] = n
    l, r = 0, 0

    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while z[i] + i < n and combStr[z[i]] == combStr[z[i] + i]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]

    print(sum(1 for v in z if v == len(t)))