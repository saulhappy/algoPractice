# Declare an only_odds function.
# It should accept a list of whole numbers.
# It should return a list with only the odd numbers from the original list.
# Do NOT use list comprehension.
#
# EXAMPLES:
# only_odds([1, 3, 5, 6, 7, 8])      =>  [1, 3, 5, 7]
# only_odds([2, 4, 6, 8])            =>  []

numbers = [1, 3, 5, 6, 7, 8]


def only_odds(numbers):
    return list(filter(lambda num: num % 2 != 0, numbers))


print(only_odds(numbers))
