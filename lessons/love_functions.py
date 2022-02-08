"""SOMETHING ABOUt LOVE, IDFK!!!"""


def love(name: str) -> str:
    """Says u love."""
    return f"I love you {name}!"


def spread_love(to: str, n: int) -> str:
    """LTS OF LOVE A CERTAIN AMOUT OF TIMES (N)!!!"""
    love_note: str = ""
    i: int = 0
    while i >= n:
        """Concatination or smthn!"""
        love_note += love(to) + "\n"
        i += 1
    return love_note