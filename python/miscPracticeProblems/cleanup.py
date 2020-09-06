# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

strings = ["cat", "er", "pillar"]


def cleanup(strings):
    result = ""
    for word in strings:
        if len(word.strip()) == 0:
            continue
        else:
            result += word.strip() + " "
    return result


print(cleanup(strings))
