"""
source: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [0]
Output: 0

Example 4:
Input: nums = [-1]
Output: -1

Example 5:
Input: nums = [-100000]
Output: -100000

"""

nums = [-2,1]

def max_sub_array(nums):
    global_max = sum(nums)

    for i, n in enumerate(nums):
        if i == 0:
            curr_sum = nums[0]
        else:
            curr_sum += n
        curr_max = max(curr_sum, global_max)
        if i == 0:
            pass
        else:
            curr_sum += n

        if curr_sum > curr_max:
            global_max = curr_sum
        
    return global_max

print(max_sub_array(nums))

# def max_sub_array_yt(nums):
#     maxSub = nums[0]
#     curSum = 0

#     for n in nums:
#         if curSum < 0:
#             curSum = 0
#         curSum += n
#         maxSub = max(maxSub, curSum)
#     return maxSub

# print(max_sub_array_yt(nums))



