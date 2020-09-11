# Declare an invert function that accepts a dictionary object.
# The function should return a new dictionary where the keys and values from the original dictionary are inverted.
# Each key should now be a value, and each value should be a key.
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
my_dict = {
    "A": "B",
    "C": "D",
    "E": "F"
}
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}


def invert(my_dict):
    new_dict = {}
    for k, v in my_dict.items():
        new_dict[v] = k
    return new_dict


print(invert(my_dict))
