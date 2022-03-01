"""EX06 - Dictionary Functions."""

__author__ = "730435749"


def invert(x_dict: dict[str, str]) -> dict[str, str]:
    """When given a dictionary, produces a new dictionary where the keys and values switch places."""
    result: dict = {}
    x_list_keys: list[str] = list()
    i: int = 0
    counter: int = 0
    for key in x_dict:
        x_list_keys.append(x_dict[key])
        result[x_dict[key]] = key
    while i < len(x_list_keys):
        while counter < len(x_list_keys):
            if x_list_keys[i] == x_list_keys[counter] and i != counter:
                return {"test": "failed"}
            counter += 1
        counter = 0
        i += 1
    return result


def favorite_color(x_dict: dict[str, str]) -> str:
    """When given a dictionary with everyone and their favorite color, returns the most common color selected."""
    colors: list[str] = list()
    color_tracker: int = 1
    color_freq: list[int] = list()
    for key in x_dict:
        colors.append(x_dict[key])
    i: int = 0
    counter: int = 0
    while i < len(colors):
        while counter < len(colors):
            if colors[i] == colors[counter] and i != counter:
                color_tracker += 1
            counter += 1
        color_freq.append(color_tracker)
        color_tracker = 1
        counter = 0
        i += 1
    i = 0
    while i < len(color_freq):
        if color_freq[i] == max(color_freq):
            return colors[i]
        else:
            i += 1


def count(x_list: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    i: int = 0
    while i < len(x_list):
        if x_list[i] in result:
            result[x_list[i]] += 1
        else:
            result[x_list[i]] = 1
        i += 1
    return result