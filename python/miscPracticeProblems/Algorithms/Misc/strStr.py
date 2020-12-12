""" source: https://leetcode.com/problems/implement-strstr/ """

haystack = "mississippi"
needle = "issip"
# 4

def strStr(haystack, needle):
    first_ocurrence = 0
    if needle not in haystack:
        return -1
    elif len(needle) == 0:
        return first_ocurrence
    elif needle == haystack:
        return first_ocurrence
    else:
        for i in range(len(haystack)):
            try:
                if haystack[i] == needle[i]:
                    first_ocurrence = i
                if needle[:len(needle)] == haystack[i:len(needle)]:
                    return first_ocurrence
                else:
                    i += len(needle)
            except IndexError:
                return first_ocurrence
            
        return first_ocurrence




print(strStr(haystack, needle))