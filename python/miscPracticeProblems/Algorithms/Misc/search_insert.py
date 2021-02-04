# source: https://leetcode.com/problems/search-insert-position/

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Input: nums = [1,3,5,6], target = 7
Output: 4

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 0
Output: 0

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1], target = 0
Output: 0

"""
nums = [1]
target = 0


def searchInsert(nums, target):
    # case where target is in nums
    if target in nums:
        return nums.index(target)
    # case where target is not in nums, and larger than anything in array
    elif target > nums[len(nums) - 1]:
        return len(nums)
    # case where target is not in nums, and smaller than anything in array
    elif target < nums[0]:
        return 0
    # case where target is not in nums, and should be somewhere in the middle
    else:
        for i in range(len(nums)):
            if nums[i] > target:
                return i

# Similar algorithm: Iterate. If the target is in the array, return i. Else, return the length of it. 
# for i in range(len(nums)):
#     if target <= nums[i]:
#         return i
# return len(nums)

# Both are O(n), but can achieve faster binary search solution of O(logN), sacrificing space


def searchInsertBinary(nums, target):
    pass
    # if target in nums:
    #     return nums.index(target)
    # else:
    #     low, high = 0, len(nums)
    #     while low < high:
    #         mid = (low + high) // 2
    #         if nums[mid] < target:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return low


print(searchInsert(nums, target))