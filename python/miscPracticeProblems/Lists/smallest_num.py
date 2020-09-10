def smallest_number(list):
    smallest = list[0]
    for num in list:
        if num < smallest:
            smallest = num
    return smallest


print(smallest_number([1, 2, 3]))
