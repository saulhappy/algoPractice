# my_dict = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }

# my_dict[4] = 'd'

# print(my_dict)

# normal recursive + memo:

message = "howdy"

def print_message(message, count=0):
    while count < 5:
        print(message)
    # print_message(message)

print(print_message(message, count + 1))

