answer = 3

print("Guess a number between 1 and 10: ")
guess = int(input())

# if guess < answer:
#     print("Guess a little higher ")
#     guess = int(input())
#     if guess == answer:
#         print("You got it!")
#     else:
#         print("Wrong again")
# elif guess > answer:
#     print("Guess a little lower ")
#     guess = int(input())
#     if guess == answer:
#         print("You got it!")
#     else:
#         print("Wrong again")
# else:
#     print("You nailed it right away!"

# REFACTOR

if guess == answer:
    print("You nailed it right away!")
else:
    if guess < answer:
        print("Guess a little higher")
    else:
        print("Guess a bit lower")
    guess = int(input())
    if guess == answer:
        print("you got it!")
    else:
        print("sorry, you didn't get it")
