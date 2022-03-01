"""Dictionaries or smthn? Idk, I cant read."""


__author__ = "730482131"


def invert(switch: dict[str, str]) -> dict[str, str]:
    """Switch a roo."""
    swap: dict[str, str]
    swap = dict()
    for x, y in switch.items():
        swap[y] = x
    return swap


def favorite_color(color: dict[str, str]) -> str:
    """Chooses most common color."""
    fav: str = ""
    tally: dict[str, int]
    tally = dict()
    for key in color:
        if color[key] in tally:
            tally[color[key]] += 1
        else:
            tally[color[key]] = 1
    amount: int = 0
    for key in tally:
        if amount < tally[key]:
            amount = tally[key]
            fav = key
    return fav


def count(things: list[str]) -> dict[str, int]:
    """Kinda what I did in the last fxn but easier."""
    digit: dict[str, int]
    digit = dict()
    i: int = 0
    while i < len(things):
        if things[i] in digit:
            digit[things[i]] += 1
            i += 1
        else:
            digit[things[i]] = 1
            i += 1
    return digit