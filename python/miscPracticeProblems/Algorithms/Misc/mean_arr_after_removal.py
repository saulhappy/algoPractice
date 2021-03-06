"""
source: https://leetcode.com/problems/mean-of-array-after-removing-some-elements/

Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.

Answers within 10-5 of the actual answer will be considered accepted.

 

Example 1:

Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
Output: 2.00000
Explanation: After erasing the minimum and the maximum values of this array, all elements are equal to 2, so the mean is 2.
Example 2:

Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
Output: 4.00000


"""
arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]

def trim_mean(arr):
        arr.sort()
        
        five_percent_of_arr = len(arr) * 0.05
        sum_elements = 0
        n_elements = 0
        
        for i in range(int(five_percent_of_arr), (len(arr)) - int(five_percent_of_arr)):
            sum_elements += arr[i]
            n_elements += 1
            
        return sum_elements / n_elements



print(trim_mean(arr))
