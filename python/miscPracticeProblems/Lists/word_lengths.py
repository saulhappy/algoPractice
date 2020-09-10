# Define a word_lengths function that accepts a string.
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]

string = "Mary Poppins was a nanny"


def word_lengths(string):
    result = []
    for word in string.split(" "):
        result.append(len(word))
    return result


print(word_lengths(string))
