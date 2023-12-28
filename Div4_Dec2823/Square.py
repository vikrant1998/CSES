import sys
import math

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = int(read_input().strip())
    i = 0
    while i < input:
        sq = int(read_input().strip())
        vals = read_input().strip().split()
        res = 0
        for v in vals: 
            res += int(v)

        res = str(math.sqrt(res))
        cmp = res.split('.')
        if cmp[1] == '0':
            print('YES')
        else:
            print('NO')
        
        i += 1