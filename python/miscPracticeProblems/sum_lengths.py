# Define a sum_of_lengths function that accepts a list of strings.
# The function should return the sum of the string lengths.
#
# EXAMPLES
# sum_of_lengths(["Hello", "Bob"])                  => 8
# sum_of_lengths(["Nonsense"])                      => 8
# sum_of_lengths(["Nonsense", "or", "confidence"])  => 20

list = ["Nonsense", "or", "confidence"]


def sum_of_lengths(list):
    result = 0
    for word in list:
        result += len(word)
    return result


print(sum_of_lengths(list))
