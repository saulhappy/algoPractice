# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

list_of_strings = [["A", "B", "C"], ["D", "E", "F", "G"]]


def fancy_concatenate(list_of_strings):
    result = ""

    for el in list_of_strings:
        if len(el) == 3:
            for char in el:
                result += char
    return result


print(fancy_concatenate(list_of_strings))
