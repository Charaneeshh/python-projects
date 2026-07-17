# Guess the Number Game
import random

secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")
print("Try to guess it!")

while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please type a number.")
        continue

    guess = int(guess)

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Great job! You guessed it!")
        break
