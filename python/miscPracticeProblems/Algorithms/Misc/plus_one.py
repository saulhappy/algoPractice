# source https://leetcode.com/problems/plus-one/

"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.


Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Input: digits = [0]
Output: [1]
"""

"""
Algorithm 1: 
create empty string, and join digits into the string. Convert to integer and add 1. 
Iterate the string, converting each char back to num, and append to results array. 
"""

digits = [0]

def plusOne1(digits):
    digits_string = ""
    result = []
    
    for num in digits:
        digits_string += str(num)
    string_num = int(digits_string) + 1
    result_string = str(string_num)

    for char in result_string:
        result.append(int(char))
    
    return result


print(plusOne1(digits))

