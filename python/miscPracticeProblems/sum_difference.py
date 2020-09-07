# Declare a sum_difference function that accepts two lists of numbers.
# It should return the difference between the sum of values in the first list and the second list
#
# EXAMPLES
# sum_difference([1, 2, 3], [1, 2, 4]) => 6 - 7 => -1
# sum_difference([4, 5], [2, 3, 6])    => 9 - 11 => -2
# sum_difference([1], [])              => 1

list1 = [1, 2, 3]
list2 = [1, 2, 4]


def sum_difference(list1, list2):
    return sum(list1) - sum(list2)


print(sum_difference(list1, list2))
