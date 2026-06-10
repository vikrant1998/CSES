import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])

    arrivals = [0] * n
    departures = [0] * n
    idx = 1
    for i in range(n):
        arrivals[i] = int(data[idx])
        departures[i] = int(data[idx + 1])
        idx += 2

    arrivals.sort()
    departures.sort()

    cur = 0
    best = 0
    j = 0
    for a in arrivals:
        # everyone who left strictly before this arrival is gone
        while departures[j] < a:
            cur -= 1
            j += 1
        cur += 1
        if cur > best:
            best = cur

    print(best)


if __name__ == "__main__":
    main()
