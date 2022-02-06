"""Totally original wordle game."""

__author__ = "730435749"


def contains_char(string_searched: str, character_searched: str) -> bool:
    """Searches for a single character within any given string."""
    assert len(character_searched) == 1
    i: int = 0
    while i < len(string_searched):
        if string_searched[i] == character_searched:
            return True  # Two return statements are used as contains_char will only express one of them depending on the user's guess.
        else:
            i += 1  # Advancing this index variable will prevents an infinite while loop on line 10.
    return False
    # contains_char needs to return a boolean value as this will allow for the distinction between when to concatenate to result a YELLOW_BOX vs a WHITE_BOX.


def emojified(a: str, b: str) -> str:
    """Searches all characters within two strings (a and b) and uses emojis to relay the relationship between the relative indices of each character searched."""
    assert len(a) == len(b)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"  
    YELLOW_BOX: str = "\U0001F7E8"    
    result: str = ""  # The result variable will be concatenated based on certain conditions, so it needs to be initialized to an empty string.
    counter: int = 0
    while counter < len(b):
        if contains_char(b, a[counter]) is False:  # Implementing the contains_char function within the emojified function allows us to quickly build off of the capabilities of the former by specifying which emoji will be concatenated based on the output of contains_char.
            result += WHITE_BOX  # WHITE_BOX is concatenated when the user's guess contains a character which is not found in the secret.
        elif a[counter] == b[counter]:
            result += GREEN_BOX  # GREEN_BOX is concatenated when a character in the user's guess and the secret share the same position in the string.
        else:
            result += YELLOW_BOX  # YELLOW_BOX is concatenated when a character in the user's guess is found in the secret but not in the correct position.
        counter += 1  # Advancing the value of the counter variable ensures we do not have an infinite while loop on line 27.
    return result


def input_guess(expected_guess_length: int) -> str:
    """Ensures the user guesses a string of proper length."""
    guess: str = input(f"Enter a {expected_guess_length} character word: ")
    while len(guess) != expected_guess_length:
        guess = input(f"That wasn't {expected_guess_length} chars! Try again: ")
    return guess  # input_guess simply returning the user's string input is so that input_guess can easily be incorporated into a variable in the main() function.


def main() -> None:  # The main() function does not need to return any particular data type as its primary purpose is to call all the above functions while keeping track of the user's turns and state of the game (i.e., a win or a loss).
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    turns: int = 1
    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        user_guess: str = input_guess(len(SECRET))  # This variable is defined with the rules and output of the input_guess function.
        if user_guess != SECRET:
            print(emojified(user_guess, SECRET))
        else:
            print(emojified(user_guess, SECRET))
            print(f"You won in {turns}/6 turns!")
            return  # This return statement ensures that once the user guesses the secret correctly, both the while loop as wells as the main() function will be exited.
        turns += 1  
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()