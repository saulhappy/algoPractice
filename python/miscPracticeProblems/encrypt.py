# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

string = "abc"


def encrypt_message(string):
    result = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for char in string:
        if char == "y":
            result += alphabet[0]
        elif char == "z":
            result += alphabet[1]
        else:
            result += alphabet[alphabet.index(char) + 2]
    return result


print(encrypt_message(string))
