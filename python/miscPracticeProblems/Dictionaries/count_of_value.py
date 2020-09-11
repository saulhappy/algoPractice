# -*- coding: utf-8 - *-
# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears
# as a value among the dictionary’s values.
#
# EXAMPLE:
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

my_dict = {"a": 5, "b": 3, "c": 5}


def count_of_value(my_dict, number):
    result = 0
    for k, _ in my_dict.items():
        if my_dict[k] == number:
            result += 1
    return result


print(count_of_value(my_dict, 5))
