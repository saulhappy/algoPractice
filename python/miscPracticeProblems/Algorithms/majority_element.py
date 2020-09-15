# -*- coding: utf-8 - *-

# source: https://leetcode.com/problems/majority-element/
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

arr = [2, 2, 1, 1, 1, 2, 2]


def majorityElement(arr):
    arr_dict = {}

    for num in arr:
        if num in arr_dict:
            arr_dict[num] += 1
        else:
            arr_dict[num] = 1
    for key, value in arr_dict.items():
        if value == max(arr_dict.values()):
            return key


print(majorityElement(arr))
