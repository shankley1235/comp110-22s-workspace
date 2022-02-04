"""Totally original wordle game."""

__author__ = 730435749


def contains_char(string_searched: str, character_searched: str) -> bool:
    """Searches for a single character within any given string."""
    assert len(character_searched) == 1
    i: int = 0
    while i < len(string_searched):
        if string_searched[i] == character_searched:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Searches all characters within two strings and uses emojis to relay the relative indices of each character searched."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    counter: int = 0
    while counter < len(secret):
        if contains_char(secret, guess[counter]) is True:
            if guess[counter] == secret[counter]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
        counter += 1
    return result


def input_guess(expected_guess_length: int) -> str:
    """Ensures the user guesses a string of proper length."""
    guess: str = input(f"Enter a {expected_guess_length} character word: ")
    while len(guess) != expected_guess_length:
        guess = input(f"That wasn't {expected_guess_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(SECRET))
        if guess != SECRET:
            print(emojified(guess, SECRET))
        else:
            print(emojified(guess, SECRET))
            print(f"You won in {turns}/6 turns!")
            return
        turns += 1  
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()