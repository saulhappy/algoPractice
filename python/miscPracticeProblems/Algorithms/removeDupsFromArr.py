"""
source: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""
nums = [0,0,1,1,1,2,2,3,3,4]
# output: 5

""" 
algorithm to try: create a new set from input, and return the length of that

"""
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    j = 1
    result = 1

    for i in range(len(nums)):
        if  nums[i] == nums[j]:
            continue
        else:
            result += 1
    return result

print(removeDuplicates(nums))
