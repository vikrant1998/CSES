if __name__ == "__main__":
    input = int(input())

    res = input
    output = [res]
    while res != 1:
        if res % 2 == 0:
            res //= 2
        else:
            res = 3 * res + 1
        output.append(res)
    result = ' '.join(str(o) for o in output)
    print(result)