"""
source: https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


"""
# Test cases:
nums1 = [2,0,2,1,1,0] # ==> [0,0,1,1,2,2]
nums2 = [2,0,1] # ==> [0,1,2]
nums3 = [0] # ==> [0]
nums4 =  [1] # ==> [1]


"""
The algorithm is the dutch national flag algorithm: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
"""

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


# two pass iteration counting number of 0s, 1s, and 2s, and replace original one
def sort_colors_counting_zeros(nums):
    zeros, ones, twos= 0,0,0
    for i in nums:
        if i == 0:
            zeros +=1
        elif i == 1:
            ones += 1
        elif i == 2:
            twos += 1

    for i in range(len(nums)):
        if zeros != 0:
            nums[i] = 0
            zeros -=1
            continue
        if ones != 0:
            nums[i] = 1
            ones -=1
            continue
        if twos != 0:
            nums[i] = 2
            twos -=1
            continue
        

print(sort_colors_counting_zeros(nums1))