# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values
# for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]
floats = [float(string) for string in values]
print(floats)

# The letters variable should store a list of 5 strings.
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Boris"
letters = [char * 3 for char in name]
print(letters)

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = [len(string) for string in elements]
print(lengths)
