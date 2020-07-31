name = input("What's your name? ")
age = int(input(f"How old are you, {name} "))
print("")
print(f"{name} is {age} years old ")

if age < 18:
    print(f"You're not old enought to vote yet, {name} ")
else:
    print(f"You can vote {name} ")
