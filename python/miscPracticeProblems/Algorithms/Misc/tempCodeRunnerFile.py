    if len(nums) == 0:
        return 0
    
    for i in range(len(nums)):
        try:
            nums[i + 1]
        except IndexError:
            break
        if nums[i] == nums[i + 1]:
            del nums[i + 1]
        else:
            i += 1
    return len(nums)