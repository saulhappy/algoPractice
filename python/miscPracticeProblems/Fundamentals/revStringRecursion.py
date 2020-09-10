text = "straw"

# iteration:


# def reverse(text):
#     start = 0
#     end = len(text) - 1
#     result = ""

#     while end != start:
#         result += text[end]
#         end -= 1

#     return result


# recursion
def reverse(text):
    if len(text) <= 1:
        return text

    return text[-1] + reverse(text[:-1])


print(reverse(text))
