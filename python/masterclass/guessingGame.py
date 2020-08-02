import random

lowerBound = 0
upperBound = 100

print(f"Guess a number between {lowerBound} and {upperBound}: ")
guess = 0

answer = random.randint(lowerBound, upperBound)
print(f"(the correct answer is {answer}. Type 0 to exit the game.)")

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("you guessed it!")
        break
    elif guess < answer:
        print("Guess a little higher")
    else:
        print("Guess a bit lower")

print("Game exited")
