"""One-Shot Wordle."""

__author__ = "730435749"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")

while len(guess) != 6:
    guess = input("That was not 6 letters! Try again: ")


if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")