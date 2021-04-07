"""
source: https://leetcode.com/problems/intersection-of-two-arrays/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

"""
### algo 1:
# make sets of nums 1 and 2. Return the intersection. 

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersection(nums1, nums2):
    return list(set(nums1).intersection(set(nums2)))

print(intersection(nums1, nums2))

