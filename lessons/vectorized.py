from __future__ import annotations

from typing import Union


class StrArray:
    Items: list[str]

    def __init__(self, items):
        self.items = items

    def __repr__(self) -> str:
        return f"strArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Add a vectorized operation that applies to all items.
        when rhs is a str, it is concatenated to every item in a strArray."""
        result: list[str] = []

        if isinstance(rhs, str):
            for i in self.items:
                result.append(i + rhs)
            return StrArray(result)
        else:
            result: list[str] = []
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
            return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
print(first + "!")
print(first + " " + last + "!")