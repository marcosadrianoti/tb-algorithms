def find_duplicate(nums):
    if len(nums) == 0 or not isinstance(nums[0], int):
        return False
    nums.sort()
    duplicated_number = None
    for id in range(0, len(nums) - 1):
        if nums[id] == nums[id + 1] and nums[id] >= 0:
            duplicated_number = nums[id]
    if duplicated_number is None:
        return False
    return duplicated_number
