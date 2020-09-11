# -*- coding: utf-8 - *-

# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary
# keys that are also found in the list.
#
# note: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
my_dict = {"a": 5, "b": 3, "c": 10}
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0


def sum_of_values(my_dict, strings):
    result = 0
    for string in strings:
        if string in my_dict:
            result += my_dict[string]
    return result


print(sum_of_values(my_dict, ["z"]))
