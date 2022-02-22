"""Some utility functions."""

__author__ = "730435749"


def only_evens(xs: list[int]) -> list[int]:
    """When given a list of integers, returns a list with only the even integers from original list."""
    result: list[int] = list()
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            result.append(xs[i])
        i += 1
    return result


def sub(xs: list[int], x: int, y: int) -> list[int]:
    """When given a list, a starting index, and an ending index, returns a truncated version of original list beginning with the element corresponding to the starting index and ending with the element preceding the ending index."""
    result: list[int] = list()
    start_index: int
    end_index: int
    if len(xs) == 0 or x > len(xs) or y <= 0:
        return []
    if x < 0:
        start_index = 0
    else:
        start_index = x
    if y > len(xs) - 1:
        end_index = len(xs) - 1
    else:
        end_index = y - 1
    while start_index <= end_index:
        result.append(xs[start_index])
        start_index += 1
    return result


def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    """Combines all elements from two lists into one list with each element of each list presented in its original order."""
    i: int = 0
    result: list[int] = list()
    if a_list != []:
        while i < len(a_list):
            result.append(a_list[i])
            i += 1
    i = 0
    if b_list != []:
        while i < len(b_list):
            result.append(b_list[i])
            i += 1
    return result
