"""
source: https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

"""

n = 5


def generateTheString(n):
    if n % 2 == 0:
        return "a" * (n - 1) + "b"
    else:
        return "a" * n


print(generateTheString(n))
