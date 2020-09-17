# -*- coding: utf-8 - *-

#  source: https://leetcode.com/problems/running-sum-of-1d-array/

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

nums = [1, 2, 3, 4]


def running_sum(nums):
    result = []

    # solution 1

    for i in range(len(nums)):
        if i == 0:
            result.append(nums[i])
        else:
            result.append(result[i - 1] + nums[i])
    return result

    # solution 2

    # result.append(nums[0])

    # for i in range(1, len(nums)):
    #     result.append(sum(nums[:i]) + nums[i])
    # return result


print(running_sum(nums))
