import random
print(" ")
print("Welcome to the guessing game!")
print(" ")
print("Pick the low end of a range of numbers to guess between: ")
lowerBound = int(input())
print("Pick the high end of a range of numbers to guess between: ")
upperBound = int(input())

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
