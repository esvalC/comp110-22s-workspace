"""We gotta test it to make sure I'm not just cheating lol. But idk how I'd cheat in a dictionary..."""


__author__ = "730482131"


from dictionary import invert
from dictionary import favorite_color
from dictionary import count
import pytest


# Invert tests
def test_invert_empty() -> None:
    """Doo a switch-a-roo but empty lol."""
    switch = {"": ""}
    assert invert(switch) == {"": ""}


def test_invert_one_set() -> None:
    """Doo a switch-a-roo withy one pair."""
    switch = {"a": "z"}
    assert invert(switch) == {"z": "a"}


def test_invert_two_sets() -> None:
    """Doo a switch-a-roo with multiple pairs."""
    switch = {"a": "z", "b": "y"}
    assert invert(switch) == {"z": "a", "y": "b"}


with pytest.raises(KeyError):
    switch = {"cal": "jackie", "potato": "jackie"}
    invert(switch)


# Fav colors!!
def test_favorite_color_empty() -> None:
    """I dont like this function so I refuse to give it a description."""
    color = {"": ""}
    assert favorite_color(color) == ""


def test_favorite_color_three() -> None:
    """Dont think because I have to do it twice that I'll cave."""
    color = {"cal": "blue", "jackie": "pink", "hugh": "blue"}
    assert favorite_color(color) == "blue"


def test_favorite_color_tie() -> None:
    """I swear, it took me forever :/ ."""
    color = {"cal": "blue", "jackie": "pink", "hugh": "blue", "kiera": "pink"}
    assert favorite_color(color) == "blue"


# count
def test_count_empty() -> None:
    """This was easier, it makes a dictionary with the amount of times a word is in a list."""
    things = [""]
    assert count(things) == {"": 0}


def test_count_double() -> None:
    """This was easier, it makes a dictionary with the amount of times a word is in a list, this one has more."""
    things = ["cal", "jackie", "jackie"]
    assert count(things) == {"cal": 1, "jackie": 2}


def test_count_lots() -> None:
    """This was easier, it makes a dictionary with the amount of times a word is in a list, this one has even more."""
    things = ["cal", "jackie", "jackie", "cal", "jackie", "jackie", "cal", "jackie", "jackie"]
    assert count(things) == {"cal": 3, "jackie": 6}