"""
source: https://leetcode.com/problems/arranging-coins/

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.

"""

n = 6
# 3

def arrangeCoins(n):
    if n == 0: return 0
    if 1 <= n <= 2: return 1
    if n == 3: return 2

    steps = 0
    counter = 0

    while n > 0:
        counter += 1
        if (steps + counter) > n: 
            return steps
        else:
            steps += 1
        n -= 1

print(arrangeCoins(n))