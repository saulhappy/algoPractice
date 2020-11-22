"""
source: https://leetcode.com/problems/longest-common-prefix/


"""

strs = ["flower","flower","flower"]
 

def longestCommonPrefix(strs):
    lngstCommonPrefix = ""

    if strs is None or len(strs) == 0:
        return lngstCommonPrefix
    
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[i]) or strs[0][i] != strs[j][i]:
                return lngstCommonPrefix
        lngstCommonPrefix += strs[0][i]
    
    return lngstCommonPrefix

print(longestCommonPrefix(strs))