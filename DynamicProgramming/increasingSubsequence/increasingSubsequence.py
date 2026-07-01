import bisect

if __name__ == "__main__":
    n = int(input())
    inp1 = input().split(' ')
    inpList = [int(x) for x in inp1]

    # tails[k] = smallest possible ending value of an increasing
    # subsequence of length k+1. tails stays sorted, so we binary-search it.
    tails = []

    i = 0
    while i < n:
        x = inpList[i]
        pos = bisect.bisect_left(tails, x)   # first index whose value is >= x
        if pos == len(tails):
            tails.append(x)                  # x beats every tail -> longest run grows
        else:
            tails[pos] = x                   # same length, smaller ending value
        i += 1

    print(len(tails))
