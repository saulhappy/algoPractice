# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings.
# For each string in the list, if the string exists as a dictionary key,
# delete the key-value pair from the dictionary.
#
# If the string does not exist as a dictionary key, avoid an error.
# The return value should be the modified dictionary object.
#
# EXAMPLE:
my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}
#
strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}


def delete_keys(dictionary, strings):
    for string in strings:
        if string in my_dict:
            del my_dict[string]
    return dictionary


print(delete_keys(my_dict, strings))
