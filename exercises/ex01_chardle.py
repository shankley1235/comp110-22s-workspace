"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730435749"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
user_character: str = input("Enter a single character: ")
if len(user_character) != 1:
    print("Error: Character must be a single character.")
    exit()
number_of_matching_chr: int = 0

print("Searching for " + user_character + " in " + user_word)

if user_character == user_word[0]:
    print(user_character + " found at index 0")
    number_of_matching_chr = number_of_matching_chr + 1
if user_character == user_word[1]:
    print(user_character + " found at index 1")
    number_of_matching_chr = number_of_matching_chr + 1
if user_character == user_word[2]:
    print(user_character + " found at index 2")
    number_of_matching_chr = number_of_matching_chr + 1
if user_character == user_word[3]:
    print(user_character + " found at index 3")
    number_of_matching_chr = number_of_matching_chr + 1
if user_character == user_word[4]:
    print(user_character + " found at index 4")
    number_of_matching_chr = number_of_matching_chr + 1
if number_of_matching_chr == 0:
    print("No instances of " + user_character + " found in " + user_word)
else:
    print(str(number_of_matching_chr) + " instances of " + user_character + " found in " + user_word)
