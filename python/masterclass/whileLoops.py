# for i in range(6):
#     print(f"i now {i}")

# i = 0
# while i < 6:
#     print(f"i is now {i}")
#     i += 1

exits = ["north", "east"]

choice = ""

while choice not in exits:
    choice = input("pick a direction: ")

print("you're out!")
