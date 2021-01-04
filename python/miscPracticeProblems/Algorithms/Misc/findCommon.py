"""
find the common elements in a sorted array with distinct elements
"""

arr1 = [1, 5, 15, 20, 30, 37, 42]
arr2 = [2, 3, 4, 5, 25, 37, 40]

"""
Brute force algorithm:
For each element in arr1, compare to each element in arr2. If they're the same append to result arr. Return result arr at end of iteration. 
Time: O(n^ (n * m), n = length of arr1 n, m = lenth of arr2). Space = O(r), length of result arr.

Optimization:
Create an object of arr1, with element as key, frequency (1) as value. 
Iterate on arr2. If that element exist in arr1, increment the key's frequency value. 
Return an array of all values in hash map with value greater than one (or two if they're all distinct). 
"""

def findCommon(arr1, arr2):
    pass

print(findCommon(arr1, arr2))

