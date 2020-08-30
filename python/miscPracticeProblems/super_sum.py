def super_sum(strings):
    sum_indices = 0
    for word in strings:
        for i in range(len(word)):
            if word[i] == "s":
                sum_indices += i
    return sum_indices


print(super_sum(["mustache"]))
