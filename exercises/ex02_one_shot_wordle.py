"""One-Shot Wordle."""

__author__ = "730435749"

secret: str = "python"
guess: str = input(f"What is your { len(secret) }-letter guess? ")
result: str = ""
i: int = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
# Defining the necessary variables.

while len(guess) != len(secret):
    guess = input(f"That was not { len(secret) } letters! Try again: ")
# The while loop above ensures the user guesses a string with the appropriate length.

while i < len(secret):
    if guess[i] == secret[i]:
        result = result + GREEN_BOX
    # The above if statement will add the green block emoji when the same character appears in the guess and secret at the same index.
    else:
        guess_check: bool = False
        alt_secret_index: int = 0
        while alt_secret_index < len(secret) and not guess_check:
            # The while loop above acts to search through each character within the secret to see if any of them match a given index of the guess.
            # The boolean variable guess_check allows us to specify whether there was a character match or not when looking at each index of the secret.
            if secret[alt_secret_index] == guess[i]:
                guess_check = True
                # The boolean variable reassignment allows us to exit the while loop and influence the results of the following if else statement.
            else:
                alt_secret_index = alt_secret_index + 1
                # Advancing the alt_secret_index ensures we avoid an infinite loop - which I experienced many times while writing this :/
        if guess_check:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        # Because the boolean variable was only reassigned when there were matching characters at different indices, the above if else statement allows us specify whether we add the white or yellow box.
    i = i + 1
    # Ensures we avoid an infinite loop in the primary while loop by advancing the index of the guess.

print(result)

if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
