answer = 3

print("Guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Guess a little higher ")
    guess = int(input())
    if guess == answer:
        print("You got it!")
elif guess > answer:
    print("Guess a little lower ")
    guess = int(input())
    if guess == answer:
        print("You got it!")
else:
    print("You nailed it!")
