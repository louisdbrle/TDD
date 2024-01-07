def maxs_3(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    return nums[-3:]


def mins_N(nums, N):
    if len(nums) < N or N <= 0:
        return []
    nums.sort()
    return nums[:N]


def prime(num):
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True
