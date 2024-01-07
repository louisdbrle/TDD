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
