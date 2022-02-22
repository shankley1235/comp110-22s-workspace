"""Testing functions for EX05."""

__author__ = "730435749"

from utils import only_evens, sub, concat


# Tests for only_evens:
def test_only_evens_all_odd() -> None:
    """Tests only_evens function when list contains all odd numbers."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []


def test_only_evens_all_even() -> None:
    """Tests only_evens function when list contains all even numbers."""
    xs: list[int] = [0, 2, 4, 6]
    assert only_evens(xs) == [0, 2, 4, 6]


def test_only_evens_some_even() -> None:
    """Tests only_evens function when list contains odd and even numbers."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_empty() -> None:
    """Tests only_evens function when given an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


# Tests for sub:
def test_sub_middle() -> None:
    """Tests sub function when starting index is not equal to 0 and when ending index is not the final index of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 1, 3) == [2, 3]


def test_sub_beginning() -> None:
    """Tests sub function when starting index is equal to 0 and when ending index is not the final index of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 0, 2) == [1, 2]


def test_sub_end() -> None:
    """Tests sub function when starting index is not equal to 0 and when ending index is the final index of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 3, 4) == [4]


def test_sub_full() -> None:
    """Tests sub function when starting index is equal to 0 and when ending index is equal to the final index of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 0, 4) == [1, 2, 3, 4]


def test_sub_impossible_indices() -> None:
    """Tests sub function when starting index is negative and ending index is greater than last index of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, -10, 20) == [1, 2, 3, 4, 5]


def test_sub_empty() -> None:
    """Tests sub function when given an empty list."""
    xs: list[int] = []
    assert sub(xs, 1, 3) == []


def test_sub_start_too_large() -> None:
    """Tests sub function when starting index is larger than the last index of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 7, 3) == []


def test_sub_end_too_small() -> None:
    """Tests sub function when ending index is less than or equal to 0, the first index of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert sub(xs, 2, 0) == []


# Tests for concat
def test_concat_not_empty() -> None:
    """Tests concat function when given two lists which are not empty."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_reverse() -> None:
    """Tests concat function when the order of the lists called is switched."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(ys, xs) == [4, 5, 6, 1, 2, 3]


def test_concat_first_empty() -> None:
    """Tests concat function when the first list called is empty."""
    xs: list[int] = []
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [4, 5, 6]


def test_concat_second_empty() -> None:
    """Tests concat function when the second list called is empty."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = []
    assert concat(xs, ys) == [1, 2, 3]


def test_concat_both_empty() -> None:
    """Tests concat function when both lists called are empty."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []