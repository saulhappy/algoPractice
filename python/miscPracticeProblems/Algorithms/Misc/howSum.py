"""
Write a function howSum that takes in a targetSum and an array of numbers as arguments. 
The function should return an array containing any combination of elements that add up to exactly the targetSum. 
If there is no combination that adds up to the targetSum, return null. 
If there are multiple combinations possible, you may return any single one. 

e.g. howSum(7, [5, 3, 4, 7]) => [3, 4] or [7]
howSum(8, [2, 3, 5]) => [2, 2, 2, 2] or [3, 5]
howSum(7, [2, 4]) => null
howSum(0, [1, 2, 3]) => []
"""



def howSum(targetSum, numbers):
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        complement = targetSum - num
        complement_result = howSum(complement, numbers)
        if complement_result != None:
            return complement_result + [num]
    return None



print(howSum(7, [2, 3])) # => [3, 2, 2]
print(howSum(7, [5, 3, 4, 7])) # => [4, 3]
print(howSum(7, [2, 4])) # => null
print(howSum(8, [2, 3, 5])) # => [2, 2, 2, 2]
# print(howSum(300, [7, 14])) # => null


