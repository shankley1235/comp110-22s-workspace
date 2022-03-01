"""Testing EX06."""

__author__ = "730435749"

from dictionary import invert, favorite_color, count


# Tests involved in the invert function.
def test_invert() -> None:
    a_dict: dict[str, str] = {"michael": "buble", "bob": "ross"}
    assert invert(a_dict) == {"buble": "michael", "ross": "bob"}


def test_invert_repetitive_keys() -> None:
    a_dict: dict[str, str] = {"michael": "jord", "kris": "jord", "Kris": "jordan"}
    assert invert(a_dict) == {"test": "failed"}


# Tests involved in the favorite_color function.
def test_favorite_color_use_case_1() -> None:
    a_dict: dict[str, str] = {"a": "Yellow", "b": "Yellow", "c": "Blue", "d": "Green", "e": "Yellow"}
    assert favorite_color(a_dict) == "Yellow"


def test_favorite_color_no_max() -> None:
    a_dict: dict[str, str] = {"a": "Yellow", "b": "Indigo", "c": "Blue", "d": "Green", "e": "White"}
    assert favorite_color(a_dict) == "Yellow"


def test_favorite_color_use_case_2() -> None:
    a_dict: dict[str, str] = {"a": "Yellow", "b": "Blue", "c": "Blue", "d": "Blue", "e": "Green", "f": "Green"}
    assert favorite_color(a_dict) == "Blue"


# Tests involved in the count function.
def test_count() -> None:
    a_list = ["a", "b", "b", "a", "c", "d", "a"]
    assert count(a_list) == {"a": 3, "b": 2, "c": 1, "d": 1}


def test_count_1() -> None:
    a_list = ["a", "b", "b", "c", "c", "d", "d"]
    assert count(a_list) == {"a": 1, "b": 2, "c": 2, "d": 2}


def test_count_2() -> None:
    a_list = ["a", "b", "c", "d"]
    assert count(a_list) == {"a": 1, "b": 1, "c": 1, "d": 1}