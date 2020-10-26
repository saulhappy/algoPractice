"""
source: https://leetcode.com/problems/rank-transform-of-an-array/

"""

arr = [37, 12, 28, 9, 100, 56, 80, 5, 12, 12]
#     [5,  3,  4,  2, 8,   6,  7,  1, 3,  3]


def arrayRankTransform(arr):
    arrCopy = arr[:]
    arrCopy.sort()
    arrSet = list(set(arr))
    arrRank = []
    seen = []

    for i in range(len(arr)):
        for j in range(len(arrCopy)):
            if arr[i] in seen:
                arrRank.append(j + 1)
            if arr[i] == arrCopy[j]:
                arrRank.append(j + 1)
                seen.append(arr[i])

    return arrRank


print(arrayRankTransform(arr))
