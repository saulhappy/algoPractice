""" search input array presence of number """

arr = [-1, 0, 3, 5, 9, 12]
num = 0

def binary_search_i(arr, num):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return False


print(binary_search_i(arr, num))