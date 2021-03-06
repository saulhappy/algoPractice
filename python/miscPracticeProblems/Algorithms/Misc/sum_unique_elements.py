"""
source:https://leetcode.com/problems/sum-of-unique-elements/

You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.
Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

"""

def sum_of_unique(arr):
    arr_map = {}
    result = 0

    for num in arr:
        if num in arr_map:
            arr_map[num] += 1
        else:
            arr_map[num] = 1
    
    for (key, value ) in arr_map.items():
        if value == 1:
            result += key
    
    return result

# OR: return sum(digit for digit in nums if nums.count(digit) == 1)

print(sum_of_unique([1,2,3,4,5]))