"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    """IDk."""
    print(powerful(2, 10))
    print("helpers.py was evaluated")


def powerful(x: float, n: float) -> float:
    """Raise x to the power of n."""
    return x ** n


# idiom to run as program
if __name__ == "__main__":
    main()
else:
    # it isnt idiomatic to have an else
    print(f"helpers.py was imported: {__name__}")