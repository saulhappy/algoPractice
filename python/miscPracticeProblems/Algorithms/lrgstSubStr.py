"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""
s = "cabbac"

def maxLengthBetweenEqualCharacters(s):
    firstSeen = {}
    maxDist = -1
    
    for index, char in enumerate(s):
        if char not in firstSeen:
            firstSeen[char] = index
        else:
            maxDist = max(index - firstSeen[char], maxDist)

    if maxDist == -1:
        return maxDist
    else:
        return maxDist - 1


print(maxLengthBetweenEqualCharacters(s))

