name = input("What's your name? ")
age = int(input(f"How old are you, {name} "))
print("")
print(f"{name} is {age} years old ")

if age < 18:
    print(f"{name}, please try to vote in {18 - age} year(s) ")
else:
    print(f"You can vote, {name}")

x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")
