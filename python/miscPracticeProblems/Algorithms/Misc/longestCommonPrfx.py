"""
source: https://leetcode.com/problems/longest-common-prefix/


"""

strs = ["flower","flight","flower", "saul"]
 

def longestCommonPrefix(strs):
    if strs is None or len(strs) == 0:
        return ""
        
    lngstCommonPrefix = strs[0]

    for i in range(1, len(strs)):
        while lngstCommonPrefix != strs[i][0 : len(lngstCommonPrefix)]:
            lngstCommonPrefix = lngstCommonPrefix[0:len(lngstCommonPrefix) - 1]
            if len(lngstCommonPrefix) == 0:
                return ""

    return lngstCommonPrefix

print(longestCommonPrefix(strs))