"""Ima test things and stuff in here yo."""

__author__ = "730482131"

from utils import only_evens
from utils import sub
from utils import concat


# Even fxn
def test_only_evens_two_evens() -> None:
    """Has two evens."""
    xs: list[int] = [1, 2, 4]
    assert only_evens(xs) == [2, 4]


def test_only_evens_two_odds() -> None:
    """Has two odds."""
    xs: list[int] = [1, 3, 4]
    assert only_evens(xs) == [4]


def test_only_evens_empty() -> None:
    """The empty one."""
    xs: list[int] = []
    assert only_evens(xs) == []


# Sum fxn
def test_sub_empty() -> None:
    """The empty one."""
    nums: list[int] = []
    assert sub(nums, 0, 0) == []


def test_sub_one() -> None:
    """Some random numbers!"""
    nums: list[int] = [2, 3, 1, 5, 6, 7, 3, 8]
    assert sub(nums, 3, 6) == [5, 6]


def test_sub_two() -> None:
    """More random numbers!"""
    nums: list[int] = [2, 3, 1, 5, 6, 7, 3, 8]
    assert sub(nums, 1, 7) == [3, 1, 5, 6, 7]


# concat
def test_concat_empty() -> None:
    """The empty one."""
    list_a: list[int] = []
    list_b: list[int] = []
    assert concat(list_a, list_b) == []


def test_concat_one() -> None:
    """1-6."""
    list_a: list[int] = [1, 2, 3]
    list_b: list[int] = [4, 5, 6]
    assert concat(list_a, list_b) == [1, 2, 3, 4, 5, 6]


def test_concat_two() -> None:
    """Beep boop, random."""
    list_a: list[int] = [1, 3, 2]
    list_b: list[int] = [4, 6, 5]
    assert concat(list_a, list_b) == [1, 3, 2, 4, 6, 5]