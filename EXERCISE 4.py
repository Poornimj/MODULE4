import random

randomNumber = random.randint(1,10)

while True:
    guess = input("Guess a number between 1 and 10:")

    try:
        guess = int(guess)

        if guess < randomNumber:
            print("Too low! Try again.")
        elif guess > randomNumber:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed the right number.")
            break
    except ValueError:
        print("Please enter a valid integer.")

