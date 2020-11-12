"""
source: https://leetcode.com/problems/rank-transform-of-an-array/

"""

arr = [37, 12, 28, 9, 100, 56, 80, 5, 12, 12]
#     [5,  3,  4,  2, 8,   6,  7,  1, 3,  3]

"""
Try this algorithm:
1. Create a non-dupe set it. Sort. 
2. For each element of set, make object with element, index + 1 as value.
3. Look up each element of input arr, append return value to result arr. 
"""

def arrayRankTransform(arr):
    pass

print(arrayRankTransform(arr))
