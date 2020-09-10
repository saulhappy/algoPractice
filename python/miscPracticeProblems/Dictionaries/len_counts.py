# Define a length_counts function that accepts a list of strings.
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters,
# 2 strings with 7 letters, and 1 string with 4 letters.

strings = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]


def length_counts(strings):
    result = {}

    for word in strings:
        if len(word) in result:
            result[len(word)] += 1
        else:
            result[len(word)] = 1
    return result


print(length_counts(strings))
