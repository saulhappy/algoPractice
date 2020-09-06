# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0

numbers = [[1, 2, 3], [4, 5]]


def nested_sum(numbers):
    result = 0
    for list in numbers:
        for num in list:
            result += num
    return result


print(nested_sum(numbers))
