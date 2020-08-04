print(" ")
print("I'm going to guess your number between 1 and 1000 in less than 10 guesses or less. ")
input("Press ENTER to continue")

low = 1
high = 1000

guesses = 1

while low != high:
    guess = (low + high) // 2

    algoResp = input(f"My guess is {guess}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess is correct ").casefold()

    if algoResp == "h":
        low = guess + 1
    elif algoResp == "l":
        high = guess - 1
    elif algoResp == "c":
        print(f"I guessed it in {guesses} guesses!")
        break
    else:
        print("Please enter h, l, or c only. ")
    guesses += 1
else:
    print(f"Your number is {low}.")
    print(f"I guessed it in {guesses} guesses!")
