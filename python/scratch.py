values = [1, 2, 3, 4, 5]
print({value: sum(values[:index + 2]) for index, value in enumerate(values)})
