""" source: https://leetcode.com/problems/implement-strstr/ """

haystack = "hello"
needle = "ll"
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
        i = 0
        while True:
            try:
                if haystack[i] == needle[0]:
                    first_ocurrence = i
                if needle == haystack[i:(i + len(needle) - 1)]:
                    return first_ocurrence
                else:
                    i += len(needle) - 1
            except IndexError:
                return first_ocurrence
            
        return first_ocurrence

print(strStr(haystack, needle))