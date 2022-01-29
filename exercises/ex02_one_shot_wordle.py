"""One-Shot Wordle."""

__author__ = "730435749"

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
result: str = ""
i: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != 6:
    guess = input("That was not 6 letters! Try again: ")

while i < len(secret):
    if guess[i] == secret[i]:
        result = result + GREEN_BOX
    else:
        guess_check: bool = False
        alt_secret_index: int = 0
        while alt_secret_index < len(secret) and not guess_check:
            if secret[alt_secret_index] == guess[i]:
                guess_check = True
            else:
                alt_secret_index = alt_secret_index + 1
        if guess_check:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    i = i + 1

print(result)

if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")