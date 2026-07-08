res = []

def backtrack(n, charCount, formedStr):
    if n == 1:
        for i in range(26):
            if charCount[i] == 1:
                formedStr.append(chr(i + 97))
                res.append(''.join(formedStr))
                formedStr.pop()
        return

    for i in range(26):
        if charCount[i] != 0:
            charCount[i] -= 1
            formedStr.append(chr(i + 97))
            backtrack(n - 1, charCount, formedStr)
            charCount[i] += 1
            formedStr.pop()


if __name__ == "__main__":
    inpList = list(input())
    charCount = [0] * 26

    for i in inpList: charCount[ord(i) % 97] += 1

    backtrack(len(inpList), charCount, [])

    print(len(res))
    for l in res:
        print(l)
