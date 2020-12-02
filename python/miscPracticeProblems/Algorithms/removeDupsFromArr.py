"""
source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""
nums = [0,0,1,1,1,2,2,3,3,4]
# output: 5

def removeDuplicates(nums):
    i = 0
    while True:
        try:
            j = nums[i + 1]
        except IndexError:
            break
        if nums[i] == nums[j]:
            del nums[i]
        else:
            i += 1
    return len(nums)


print(removeDuplicates(nums))
