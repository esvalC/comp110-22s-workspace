"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730482131"


class Simpy:
    """Simpy!"""
    values: list[float]

    def __init__(self, values: list[float]):
        """I dont like doctrings, this does something!"""
        self.values = values

    def __str__(self) -> str:
        """I dont like doctrings, this does something!"""
        return f"Simpy({self.values})"

    def fill(self, value: float, repeat: int) -> None:
        """I dont like doctrings, this does something!"""
        assert repeat != 0
        self.values = []
        i: int = 0
        while i < repeat:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """I dont like doctrings, this does something!"""
        assert step != 0.0
        self.values: list[float]
        n: int = 0
        value: float = 0.0
        while abs(value) < abs(stop):
            value = (step * n + start)
            if abs(value) < abs(stop):
                self.values.append(value)
            n += 1

    def sum(self) -> float:
        """I dont like doctrings, this does something!"""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """I dont like doctrings, this does something!"""
        output = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for value in self.values:
                output.values.append(value + rhs.values[i])
                i += 1
            return output
        else:
            for value in self.values:
                output.values.append(value + rhs)
            return output

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """I dont like doctrings, this does something!"""
        output = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for value in self.values:
                output.values.append(value ** rhs.values[i])
                i += 1
            return output
        else:
            for value in self.values:
                output.values.append(value ** rhs)
            return output

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """I dont like doctrings, this does something!"""
        output: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for value in self.values:
                if (value == rhs.values[i]):
                    output.append(True)
                    i += 1
                else:
                    output.append(False)
                    i += 1
            return output
        else:
            for value in self.values:
                if (value == rhs):
                    output.append(True)
                else:
                    output.append(False)
            return output

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """I dont like doctrings, this does something!"""
        output: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            for value in self.values:
                if (value > rhs.values[i]):
                    output.append(True)
                    i += 1
                else:
                    output.append(False)
                    i += 1
            return output
        else:
            for value in self.values:
                if (value > rhs):
                    output.append(True)
                else:
                    output.append(False)
            return output

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """I dont like doctrings, this does something!"""
        i: float = 0.0
        if isinstance(rhs, int):
            output: float
            for value in self.values:
                if i == rhs:
                    output = value
                    return output
                else:
                    i += 1
        else:
            outputsi = Simpy([])
            i: int = 0
            for value in rhs:
                if value is True:
                    outputsi.values.append(self.values[i])
                    i += 1
                else:
                    i += 1
            return outputsi