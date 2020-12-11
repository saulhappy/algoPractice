""" source: https://leetcode.com/problems/implement-strstr/ """

haystack = ""
needle = ""


def strStr(haystack, needle):
    if needle not in haystack:
        return -1

    if len(needle) == 0:
        return 0

    for i in range(len(haystack)):
        index = 0
        if needle[0] == haystack[i]:
            index = i
            for j in range(1, len(needle)):
                if needle[j] != haystack[i + 1]:
                    return -1
        else:
            continue
        return index

    return "it's in there"


print(strStr(haystack, needle))