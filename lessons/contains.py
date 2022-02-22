"""Example of a function that searches thru a list."""

# Define function names contains
# Two parameters:
# 1. Needle: str we are looking for
# 2. Haystack: list we are looking thru
# Algo:
#   for each item in haystack, we'll test if equal to needle, if so return True
#   after returning all items, return False, because not found
# Returns Turue if needle in haystack, False otherwise


def contains(needle: str, haystack: list[str]) -> bool:
    """Searches for a string in a list of strings."""
    for item in haystack:
        if item == needle:
            return True
    return False