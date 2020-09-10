# Declare a long_word_in_collection function that accepts a list and a string.
# The function should return True if
#   - the string exists in the list AND
#   - the string has more than 4 characters.
#
words = ["cat", "dog", "rhino"]
# long_word_in_collection(words, "rhino")  => True
# long_word_in_collection(words, "cat")    => False
# long_word_in_collection(words, "monkey") => False


def long_word_in_collection(list, string):
    return string in words and len(string) > 4


print(long_word_in_collection(words, "cat"))
