# Declare a sum_of_evens_and_odds function that accepts a tuple of numbers.
# It should return a tuple with two numeric values:
# -- the sum of the even numbers
# -- the sum of the odd numbers.
#
# sum_of_evens_and_odds((1, 2, 3, 4))   => (6, 4)
# sum_of_evens_and_odds((1, 3, 5))      => (0, 9)
# sum_of_evens_and_odds((2, 4, 6))      => (12, 0)

numbers = (1, 2, 3, 4)


def sum_of_evens_and_odds(numbers):
    evens = sum(list(filter(lambda num: num % 2 == 0, numbers)))
    odds = sum(list(filter(lambda num: num % 2 != 0, numbers)))
    return (evens, odds)


print(sum_of_evens_and_odds(numbers))
