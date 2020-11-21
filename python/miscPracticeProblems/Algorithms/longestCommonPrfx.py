"""
source: https://leetcode.com/problems/longest-common-prefix/

algorithm to try: take the first element of str, split.
For each char is that first split element:
If that char is equal to the char of the split element of next str, 
add to result string. If not, continue. Return the string at the end of the iteration.

"""

strs = ["saul","flower","flow","flight"]
 

def longestCommonPrefix(strs):
    result = ""

    for i in range(len(strs)):
        currentWord = strs[i]
        for j in range(len(currentWord)):
            if currentWord[j] == strs[i + 1][j]:
                result += currentWord[j]
            else:
                continue
    return result





print(longestCommonPrefix(strs))