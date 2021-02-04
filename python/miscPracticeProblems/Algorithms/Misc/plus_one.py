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

Works for most uses cases, but not edge case: [0,0] (doesn't seem like a real num?)
Output is [1], expected is [0, 1]. [0,0,0] => [0, 0, 1]; [0, 0, 9] => [0, 1, 0]
"""

"""
Algorithm 2:
create copy of digits
Pop the last element of copy. 
If it's 9, pop last element again, add 1, and append back to copy. 
Else, add one, append back to copy
return copy.

"""

digits = [1, 9]

def plus_One_1(digits):
    digits_string = ""
    result = []
    
    for num in digits:
        digits_string += str(num)
    string_num = int(digits_string) + 1
    result_string = str(string_num)

    for char in result_string:
        result.append(int(char))
    
    return result

def plus_One_2(digits):
    result = digits[:]

    last_el = result.pop()

    if last_el == 9:
        if len(result) == 0:
            return [1, 0]
        else:
            second_last = result.pop()
            last_two = str(second_last) + str(last_el)
            last_two = str(int(last_two) + 1)
            result.append(int(last_two[0]))
            result.append(int(last_two[1]))
            return result
    else:
        last_el += 1
        result.append(last_el)
        return result




print(plus_One_2(digits))

