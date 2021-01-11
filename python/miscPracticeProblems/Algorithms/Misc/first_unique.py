# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.


"""
Algorithm to try:
if len of string == 0, return -1
create array of special characters. Create hash. Iterate.
If current char is in special character array, continue. 
Add char with char as key, 1 or += 1 as value. 
End of iteration
Iterate string again with enumerate. 
If char in hash with value of 1, return index. 
"""

string = "hi! i am a string!"

def first_unique(string): 
    pass

print(first_unique(string))

