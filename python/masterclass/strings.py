# printing with input:
greeting = "Hello"
name = input("Please enter your name: ")

print(greeting + " " + name)

# escape character
splitString = "this string is being\nover many\n lines"
print(splitString)

# tab characters
tabbedNumbers = "1\t2\t3\t4\t5"
print(tabbedNumbers)

# triple quotes removes need for escaping...
anotherSplitString = """This is another
  string
that's being split over
many lines. """

print(anotherSplitString)
