"""
https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""
s = "cabbac"

def maxLengthBetweenEqualCharacters(s):
    lastSeen = {}
    maxDist = -1
    
    for index, char in enumerate(s):
        if char not in lastSeen:
            lastSeen[char] = index
    return lastSeen

print(maxLengthBetweenEqualCharacters(s))

