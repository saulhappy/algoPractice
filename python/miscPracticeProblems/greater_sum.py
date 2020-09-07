# Declare a greater_sum function that accepts two lists of numbers.
# It should return the list with the greatest sum.
# You can assume the lists will always have different sums.
#
# EXAMPLES
# greater_sum([1, 2, 3], [1, 2, 4]) => [1, 2, 4]
# greater_sum([4, 5], [2, 3, 6])    => [2, 3, 6]
# greater_sum([1], [])              => [1]

list1 = [1, 2, 3]
list2 = [1, 2, 4]


def greater_sum(list1, list2):
    sumL1 = sum(list1)
    sumL2 = sum(list2)
    if sumL1 > sumL2:
        return list1
    else:
        return list2


print(greater_sum(list1, list2))
