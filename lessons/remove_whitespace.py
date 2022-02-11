"""Doc."""


def remove_ws() -> str:
    word: str = input("Give me a word: ")
    new_word: str = ""
    i: int = 0
    while i < len(word):
        if word[i] != " ":
            new_word += word[i]
        i += 1
    return new_word