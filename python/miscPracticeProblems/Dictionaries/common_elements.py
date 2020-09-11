# -*- coding: utf-8 - *-

# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
my_dict = {
    "A": "K",
    "B": "D",
    "C": "A",
    "D": "Z"
}
#
# common_elements(my_dict) => ["A", "D"]

# saul version
# def common_elements(my_dict):
#     result = []
#     for k in my_dict.keys():
#         if k in my_dict.values():
#             result.append(k)
#     return result

# refactor:


def common_elements(my_dict):
    return [key for key in my_dict.keys() if key in my_dict.values()]


print(common_elements(my_dict))
