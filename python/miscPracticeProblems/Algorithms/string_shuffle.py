"""
source: https://leetcode.com/problems/shuffle-string/

Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.

Example 1:

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
"""

s = "aiohn"
indices = [3, 1, 4, 2, 0]


def restoreString(s, indices):
    new_string = ""
    for i in range(len(indices)):
        new_string += s[indices[i]]
    return new_string


print(restoreString(s, indices))
