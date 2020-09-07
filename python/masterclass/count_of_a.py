# Declare a count_of_a function that accepts a list of strings.
# It should return a list with counts of how many “a” characters appear per string.
# Do NOT use list comprehension.
#
# EXAMPLES:
# count_of_a(["alligator", "aardvark", "albatross"])    => [2, 3, 2]
# count_of_a(["plywood"])                               => [0]
# count_of_a([])                                        => []

strings = ["alligator", "aardvark", "albatross"]


def count_of_a(strings):
    return list(map(lambda string: string.count("a"), strings))


print(count_of_a(strings))
