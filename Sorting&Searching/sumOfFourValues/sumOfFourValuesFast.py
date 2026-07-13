import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = int(data[1])
    vals = [int(x) for x in data[2:2 + n]]

    # Four indices a < b < c < d with vals[a]+vals[b]+vals[c]+vals[d] == s.
    # Split into two pair-sums:  (vals[a]+vals[b]) + (vals[c]+vals[d]) == s.
    #
    # Fix c and d as the two larger indices (c < d). For the lookup to return a
    # valid pair (a, b) we need b < c, i.e. the dict must only contain pairs whose
    # BOTH indices are < c. So we grow the dict one step behind c:
    #
    #   before handling a given c, insert every pair (a, c-1) with a < c-1.
    #
    # That keeps the invariant "every stored pair has both indices <= c-1 < c".
    # Then for each d > c we query s - vals[c] - vals[d]; a hit gives a<b<c<d
    # with all four distinct. Each c does O(n) inserts + O(n) queries -> O(n^2).
    seen = {}  # pair_sum -> (a+1, b+1), 1-based, for a fully-registered smaller pair
    for c in range(n):
        # Register pairs whose larger index is exactly c-1 (so both indices < c).
        b = c - 1
        if b >= 1:
            vb = vals[b]
            for a in range(b):
                pair_sum = vals[a] + vb
                if pair_sum not in seen:
                    seen[pair_sum] = (a + 1, b + 1)

        # Now look for a matching later pair (c, d) with d > c.
        base = s - vals[c]
        for d in range(c + 1, n):
            complement = base - vals[d]
            if complement in seen:
                a, b = seen[complement]
                print(a, b, c + 1, d + 1)
                return

    print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
