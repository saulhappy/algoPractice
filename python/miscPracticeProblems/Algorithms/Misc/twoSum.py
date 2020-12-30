"""
source: https://leetcode.com/problems/two-sum/

"""

nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [i, seen[target-num]]
        seen[num] = i 


print(twoSum(nums, target))