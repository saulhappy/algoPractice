"""
source: https://leetcode.com/problems/reverse-vowels-of-a-string/
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""
"""
algorithm to try: 
- create a vowels array with both cases
- create a vowels stack
- iterte string, fill stack with the vowels of the string
- iterate string again: if you see a vowel, pop a vowel out of the stack and replace the char of the string with the vowel just poppped
return new string

"""
def reverse_vowels(s):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    vowels_stack = []
    rev_str_arr = []

    for i in range(len(s)):
         if s[i] in vowels:
             vowels_stack.insert(0, s[i])
    
    for i in range(len(s)):
        if s[i] in vowels:
            rev_str_arr.append(vowels_stack.pop(0))
        else:
            rev_str_arr.append(s[i])
    
    return ''.join(rev_str_arr)

print(reverse_vowels("hello"))
