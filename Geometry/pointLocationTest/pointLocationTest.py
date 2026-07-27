# Input:
# 3
# 1 1 5 3 2 3
# 1 1 5 3 4 1
# 1 1 5 3 3 2

# Output:
# LEFT
# RIGHT
# TOUCH

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        inp1 = input().split(' ')
        p1 = (int(inp1[0]), int(inp1[1]))
        p2 = (int(inp1[2]), int(inp1[3]))
        p3 = (int(inp1[4]), int(inp1[5]))

        p2_1 = (p2[0] - p1[0], p2[1] - p1[1])
        p3_1 = (p3[0] - p1[0], p3[1] - p1[1])

        p_cross = (p3_1[0] * p2_1[1]) - (p3_1[1] * p2_1[0])
        if p_cross < 0:
            print('LEFT')
        elif p_cross > 0:
            print('RIGHT')
        else:
            print('TOUCH')