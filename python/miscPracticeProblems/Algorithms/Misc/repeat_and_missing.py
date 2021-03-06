"""
source: https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

Examples: 

Input: arr[] = {3, 1, 3}
Output: Missing = 2, Repeating = 3
Explanation: In the array, 
2 is missing and 3 occurs twice 

Input: arr[] = {4, 3, 6, 2, 1, 1}
Output: Missing = 5, Repeating = 1

"""

#TEST CASES
arr1=[3,1,3] # => missing = 2, repeating = 3
arr2=[4, 3, 6, 2, 1, 1] # => missing = 5, repeating = 1


# works for these test cases. would need try/catch at end of arrays...
# or if missing is assumed to be start or end of array

def find_missing_repeating(arr):
    missing = None
    repeating = None

    arr = sorted(arr)

    # for missing
    for i in range(len(arr)):
        if arr[i+1] >= arr[i] + 2:
            missing = arr[i] + 1
            break
    
    # for repeating
    for i in range(len(arr)):
        if arr[i] == arr[i+1]:
            repeating = arr[i]
            break
                    
    return f"Missing = {missing}   Repeating = {repeating}"


print(find_missing_repeating(arr1))