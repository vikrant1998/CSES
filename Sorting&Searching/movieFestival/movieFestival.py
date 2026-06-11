if __name__ == "__main__":
    n = int(input())
    movies = []
    for i in range(n):
        st, ed = map(int, input().split())
        movies.append([st, ed])

    movies.sort(key=lambda item: item[1])

    count = 0
    last_end = 0
    for st, ed in movies:
        if st >= last_end:
            count += 1
            last_end = ed

    print(count)