import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = int(read_input().strip())
    V = {'a','e'}
    C = {'b','c','d'}

    i = 0
    while i < input:
        num = int(read_input().strip())
        txt = list(read_input().strip())

        res = []
        idx = 0
        flag = 0
        while (len(res) != 0 and res[-1][1] == -1) or (len(res) != len(txt) and idx < len(txt)):
            if flag == 0:
                if idx < len(txt) and txt[idx] in C\
                    and idx + 1 < len(txt) and txt[idx + 1] in V:
                    res.append(([txt[idx], txt[idx + 1]], 2))
                    idx += 2
                    flag = 1
            else:
                if idx < len(txt) and txt[idx] in C\
                    and idx + 1 < len(txt) and txt[idx + 1] in V and res[-1][1] != -1:
                    res.append(([txt[idx], txt[idx + 1]], 2))
                    idx += 2
                elif idx < len(txt) and txt[idx] in C\
                    and idx + 1 < len(txt) and txt[idx + 1] in V\
                    and idx + 2 < len(txt) and txt[idx + 2] in C:
                    if res[-1][1] == -1:
                        res.pop()
                    res.append(([txt[idx], txt[idx + 1], txt[idx + 2]], 3))
                    idx += 3
                else:
                    val = res[-1]
                    res.pop()
                    if val[1] == 2:
                        idx -= 2
                        if idx < len(txt) and txt[idx] in C\
                            and idx + 1 < len(txt) and txt[idx + 1] in V\
                            and idx + 2 < len(txt) and txt[idx + 2] in C:
                            res.append(([txt[idx], txt[idx + 1], txt[idx + 2]], 3))
                            idx += 3
                    else:
                        idx -= 3
                        res.append([1,2,3], -1)

        tmpStr = ''
        for r in res:
            tmpStr += (''.join(r[0])) + '.'
        print(tmpStr[:-1])
        i += 1