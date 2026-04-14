secret = 7
tries = 0

guess = int(input(" Guess the number between 1 and 10: "))

while guess != secret:
    tries = tries + 1
    if guess > secret:
        print("Too high!")
    else:
        print("Too low!")

    guess = int(input(" Guess the number between 1 and 10: "))
print("Correct guess!")
print("You made", tries, "guesses.")
