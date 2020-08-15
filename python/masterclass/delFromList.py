data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, value in enumerate(data):
    print(index, value)

# delete first two elements:
# del data[0:2]

print()

for index, value in enumerate(data):
    if value % 2 == 0:
        print(index, value)
