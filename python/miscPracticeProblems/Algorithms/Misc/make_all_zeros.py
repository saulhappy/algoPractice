"""
helper function to turn all elements of an array to zeros

"""

arr1=[1,2,3]
arr2=[]
arr3=[1,0]


def make_zeros(arr):
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i] = 0
    return arr

print(make_zeros(arr1))