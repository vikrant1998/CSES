import sys

def read_input():
    input = sys.stdin.readline()
    return input

if __name__ == "__main__":
    input = int(read_input())
    if input == 2:
        print('NO')
        sys.exit()
    res = 'YES' if not input % 2 else 'NO'
    print(res)