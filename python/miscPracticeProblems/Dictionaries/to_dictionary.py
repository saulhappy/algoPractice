# -*- coding: utf-8 - *-

# Define a to_dictionary function that accepts a list of strings.
# The function should return a dictionary where the keys are the strings
# and the values are their original index positions in the list.
#
# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}

strings = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]


def to_dictionary(strings):
    my_dict = {}
    for i, detective in enumerate(strings):
        my_dict[detective] = i
    return my_dict


print(to_dictionary(strings))
