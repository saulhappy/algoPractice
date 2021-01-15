""" source: https://leetcode.com/problems/monotonic-array/#:~:text=An%20array%20is%20monotonic%20if,%3E%3D%20A%5Bj%5D%20."""


def is_monotonic(arr):
    i = 0

    while True: 
        try:
            arr[i + 1]
        except IndexError:
            break

        if arr[i] >= arr[i + 1]:
            i += 1
            continue

        if arr[i] <= arr[i + 1]:
            i += 1
            continue

        else:
            return False
    return True

# print(is_monotonic([1, 2, 3, 4, 5])) # True
print(is_monotonic([1, 2, 1, 4, 5])) # False
# print(is_monotonic([10, 9, 8, 7, 6])) # True
# print(is_monotonic([1, 2, 3, 4, 5])) # True

