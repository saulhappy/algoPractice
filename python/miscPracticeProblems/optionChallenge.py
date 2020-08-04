meals = ["pizza", "steak", "chicken and mash",
         "sandwich", "hamburger", "pasta"]

selection = ""

print("Select a meal option:")
while selection != 0:

    for i in range(len(meals)):
        print(f"{i + 1}. {meals[i]}")
    else:
        print("0. Quit")
    selection = int(input())
    if selection not in range(len(meals)):
        print("Please make valid choice")
    else:
        print(f"You chose {meals[selection - 1]}")
