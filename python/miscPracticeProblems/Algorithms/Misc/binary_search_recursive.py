arr = [-1, 0, 3, 5, 9, 12]
num = 9

def binary_search_r(arr, num):
    # base case:
    if len(arr) == 0 or (len(arr) == 1 and arr[0] != num):
        return False

print(binary_search_r(arr, num))