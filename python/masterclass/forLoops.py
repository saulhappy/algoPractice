balance = "9,564,564,323.23"
seperators = ""

for char in balance:
    if not char.isdigit():
        seperators += char

print(seperators)
