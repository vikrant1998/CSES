if __name__ == "__main__":
    n = int(input())
    count = 0
    power = 5
    while power <= n:
        count += n // power
        power *= 5

    print(count)