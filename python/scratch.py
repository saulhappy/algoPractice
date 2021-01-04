arr1 = [1, 5, 15, 20, 30, 37, 42]
arr2 = [2, 3, 4, 5, 25, 37, 40]

arr1Set = set(arr1)
arr2Set = set(arr2)

print(list(arr1Set.intersection(arr2Set)))
