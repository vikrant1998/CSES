if __name__ == "__main__":
    n = int(input())

    for i in range(2 ** n):
        graycode = i ^ (i >> 1)
        print(bin(graycode)[2:].zfill(n))