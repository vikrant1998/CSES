import sys


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    q = int(data[idx]); idx += 1

    # arr[p] = the value sitting at position p (1-indexed for convenience)
    arr = [0] * (n + 1)
    for p in range(1, n + 1):
        arr[p] = int(data[idx]); idx += 1

    # pos[v] = the position where value v currently lives.
    # this is the inverse of arr, and lets us ask "where is value v?" in O(1).
    pos = [0] * (n + 2)
    for p in range(1, n + 1):
        pos[arr[p]] = p

    # A "break" is a value v where the next value v+1 sits to its LEFT
    # (pos[v] > pos[v+1]) -- meaning you can't grab v+1 right after v in the
    # same left-to-right pass, so a new round must start there.
    # Total rounds = number of breaks + 1.
    breaks = 0
    for v in range(1, n):
        if pos[v] > pos[v + 1]:
            breaks += 1

    out = []
    for _ in range(q):
        i = int(data[idx]); idx += 1
        j = int(data[idx]); idx += 1

        a, b = arr[i], arr[j]  # the two VALUES currently at positions i and j

        # A swap only moves values a and b, so the only breaks that can change
        # are the ones where a or b is one half of a consecutive-value pair:
        #   (a-1,a), (a,a+1), (b-1,b), (b,b+1)
        # We track those by the smaller value of each pair: {a-1, a, b-1, b}.
        # The set dedups the overlap when a and b are themselves consecutive.
        affected = {a - 1, a, b - 1, b}

        # STEP 1: remove the old break-status of each affected pair, because
        # after the swap these pairs may no longer be breaks.
        for v in affected:
            if 1 <= v < n and pos[v] > pos[v + 1]:
                breaks -= 1

        # STEP 2: perform the swap. Update BOTH arrays so they stay consistent:
        # arr (position -> value) and pos (value -> position) are inverses.
        arr[i], arr[j] = b, a
        pos[a], pos[b] = j, i

        # STEP 3: re-add the break-status of the same pairs in their new state.
        for v in affected:
            if 1 <= v < n and pos[v] > pos[v + 1]:
                breaks += 1

        # answer for this query: rounds = breaks + 1
        out.append(str(breaks + 1))

    sys.stdout.write("\n".join(out) + "\n")


main()
