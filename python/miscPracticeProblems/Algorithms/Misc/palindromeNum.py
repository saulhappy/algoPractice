"""
source: https://leetcode.com/problems/palindrome-number/
"""
x = -121

def isPalindrome(x):
    if x < 0:
        return False
    else:
        return x == int(str(x)[::-1])

print(isPalindrome(x))