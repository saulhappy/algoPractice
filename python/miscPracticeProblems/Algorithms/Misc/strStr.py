""" source: https://leetcode.com/problems/implement-strstr/ """

haystack = "abc"
needle = "c"
# 2

# haystack = "mississippi"
# needle = "issip"
# 4

"""
Solution works locally, but fails in leetcode for unknown reason. Simple solution is 
using .index() or .find() methods
"""

def strStr(haystack, needle):
    first_ocurrence = 0
    if needle not in haystack:
        return -1
    elif len(needle) == 0:
        return first_ocurrence
    elif needle == haystack:
        return first_ocurrence
    else:
        i = 0
        while True:
            try:
                if haystack[i] == needle[0]:
                    first_ocurrence = i
                if len(needle) == 1 and needle == haystack[i]:
                    return first_ocurrence
                if needle == haystack[i:(i + len(needle))]:
                    return first_ocurrence
                else:
                    i += 1
            except IndexError:
                return first_ocurrence
            
        return first_ocurrence

print(strStr(haystack, needle))