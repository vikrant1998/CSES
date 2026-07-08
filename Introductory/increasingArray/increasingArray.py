if __name__ == "__main__":
    n = int(input())
    nums = input().split(' ')
    nums = [int(num) for num in nums]

    i = 0
    moves = 0
    while i < len(nums):
        if i - 1 >= 0 and nums[i-1] > nums[i]:
            diff = nums[i-1] - nums[i]
            moves += diff
            nums[i] += diff
        i += 1
    print(moves)