# balance = "9,564,564,323.23"
# seperators = ""

# for char in balance:
#     if not char.isdigit():
#         seperators += char

# print(seperators)

# for i in range(1, 6):
#     print(f"the number is now {i}")


shoppingItems = ["milk", "pasta", "eggs", "spam", "bread", "rice"]


for i in range(len(shoppingItems)):
    print(i)
print("==========================")

for item in shoppingItems:
    print(item)
print("==========================")

for index in range(len(shoppingItems)):
    print(index, shoppingItems[index])
print("==========================")
