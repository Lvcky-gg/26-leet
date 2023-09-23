def removeDuplicates(nums):
    pointer = len(nums) - 1
    while pointer > 0:
        if nums[pointer] == nums[pointer - 1]:
            nums.pop(pointer)
        pointer -= 1
    return nums