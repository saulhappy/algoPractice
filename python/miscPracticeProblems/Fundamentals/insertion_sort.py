"""
Pseudocode:
for j = 2 to A.length:
    key = A[j]
    # insert A[j] into sorted sequence A[1..j - 1]
    i = j - 1
    while i > 0 and A[j] > key:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
"""

arr = [3, 56, 7, 12, 9, 2, 9, 82, 20] # => [2, 3, 7, 9, 9, 20, 56, 82] 

def insertion_sort(arr):
    pass

print(insertion_sort(arr))

