"""Example of test subject!"""


def sum(xs: list[float]) -> float:
    """Completes the sum of a list."""
    total: float = 0
    for x in xs:
        total += x
    return total