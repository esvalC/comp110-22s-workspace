"""TBH idk what utils means besides the measurment of happiness so lets see where this goes."""

__author__ = "730482131"


def only_evens(xs: list[int]) -> list[int]:
    """Find the even numbers!"""
    i: int = 0

    while i < len(xs):
        if xs[i] % 2 == 0:
            i += 1
        else:
            xs.pop(i)
            if i > len(xs):
                i += 1

    return xs


def sub(nums: list[int], x: int, y: int) -> list[int]:
    """If this function was used on a watermellon, it could tell you that the red is between the green shell."""
    final: list[int] = list()
    if len(nums) == 0 or x > len(nums) or y <= 0:
        return final
    if x < 0:
        x = 0
    if y > len(nums):
        y = len(nums)
    i: int = x
    while i < y and i <= len(nums):
        final.append(nums[i])
        i += 1
    return final


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """Puts things together, kinda like legos, but different."""
    last: list[int] = list()
    last = list_a
    i: int = 0
    while i < len(list_b):
        last.append(list_b[i])
        i += 1
    return last