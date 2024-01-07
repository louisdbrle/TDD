def maxs_3(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    return nums[-3:]
