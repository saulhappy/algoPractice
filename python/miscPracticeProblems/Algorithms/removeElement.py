"""
source: https://leetcode.com/problems/remove-element/

"""


nums = [3,2,2,3]
val = 3

def removeElement(nums, val):
    i = 0

    while True:
        try:
            nums[i]
        except IndexError:
            break
        if nums[i] == val:
            del nums[i]
        else:
            i += 1
    return len(nums)



print(removeElement(nums, val))