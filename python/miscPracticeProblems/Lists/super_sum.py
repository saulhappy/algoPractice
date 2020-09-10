# def super_sum(strings):
#     sum_indices = 0
#     for word in strings:
#         for i in range(len(word)):
#             if word[i] == "s":
#                 sum_indices += i
#                 break
#     return sum_indices


def super_sum(strings):
    result = 0
    for word in strings:
        if "s" in word:
            result += word.find("s")
    return result


print(super_sum(["mustache", "pessimist"]))
