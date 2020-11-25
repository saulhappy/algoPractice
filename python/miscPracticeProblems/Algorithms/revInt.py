"""
source: https://leetcode.com/problems/reverse-integer/

"""

"""
first algorithm to try:
turn int to string, iterate, for each char starting from the back, append to new string, then convert to int.
edge cases: zero, postive, negative

"""

x = 1534236469

def reverseInt(x):
    result = 0

    if x == 0:
        return result
    if x > 0:
        result = int(str(x)[::-1])
    if x < 0:
        result = int(("-" + str(x * -1)[::-1]))

    if result <= -2**31 or result >= 2**31:
        return 0
    else:
        return result


print(reverseInt(x))