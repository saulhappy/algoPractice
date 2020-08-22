word = "helicopter"


def vowel_count(word):
    return word.count("a") + word.count("e") + word.count("i") \
        + word.count("o") + word.count("u")


print(vowel_count(word))
