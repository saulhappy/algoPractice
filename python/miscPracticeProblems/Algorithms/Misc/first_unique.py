# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.


"""
Algorithm to try:
if len of string == 0, return -1
create array of special characters. Create hash. Iterate.
If current char is in special character array, continue. 
Add char with char as key, index as value. 
End of iteration
Iterate string again with enumerate. 
If char in hash with value of 1, return index. 
"""

def first_unique(string): 
    special_chars = ['"', '!', '@', '#', '?', ',', '.', '/', '$', '%', " "]
    char_hash = {}

    if len(string) == 0:
        return -1

    for char in string:
        if char in special_chars:
            continue
        if char not in char_hash.keys():
            char_hash[char] = 1
        else:
            char_hash[char] += 1

    for i, char in enumerate(string):
        if char in char_hash.keys() and char_hash[char] == 1:
            return i

    return -1

"""
ANOTHER ALGORITHM:
Iterate: if current character is in the rest of the string, continue. 
Otherwise, return the current i. If at the end can't find anything, 
return -1
"""
def first_unique_slice(string):
    for i, char in enumerate(string):
        if char in string[i + 1:]:
            continue
        else:
            return i
    return -1


print(first_unique('alphabet'))
print(first_unique('barbados'))
print(first_unique('crunchy'))
print(first_unique(''))


print(first_unique_slice('alphabet'))
print(first_unique_slice('barbados'))
print(first_unique_slice('crunchy'))
print(first_unique_slice(''))