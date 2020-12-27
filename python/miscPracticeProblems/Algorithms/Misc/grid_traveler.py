""" looks same as leetcode unique paths 
source: https://leetcode.com/problems/unique-paths/ 
given a c x r grid, where you are located in the top left corner, and can only move left and right,
how many paths can  you take to reach the bottom right corner?
"""

c = 15
r = 15

"""
Going down reduces playable areas by a row, going right by a column.
At 1x1, we do nothing: start is same as end, or 1
At any 0 coordinate, there's nothing to do: it's not a grid, or 0 

"""

def grid_traveler(r, c):
    if c == 1 and r == 1:
        return 1
    if c == 0 or r == 0:
        return 0
    else:
        return grid_traveler(r - 1, c) + grid_traveler(r, c -1)
    
    

print(grid_traveler(c, r))

