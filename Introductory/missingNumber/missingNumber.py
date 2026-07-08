if __name__ == "__main__":
    n = int(input())
    nums = input().split(' ')
    nums = [int(num) for num in nums]

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing_number = expected_sum - actual_sum
    print(missing_number)