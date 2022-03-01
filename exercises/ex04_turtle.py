"""Supposed to be an underwater scene..."""

__author__ = "730482131"

from random import randint
from turtle import Turtle, colormode, done

colormode(255)
ja: Turtle = Turtle()
ja.speed(0)


def stick_figure(x: float, y: float, size: float) -> None:
    """Makes a stick figure lol."""
    assert size <= 1
    ja.penup()
    ja.goto(x, y)
    ja.pendown()
    ja.color("black")

    ja.left(60)
    ja.forward(100 * size)
    ja.right(120)
    ja.forward(100 * size)
    ja.right(180)
    ja.forward(100 * size)
    ja.right(30)
    ja.forward(105 * size)
    ja.right(90)
    ja.forward(100 * size)
    ja.right(180)
    ja.forward(200 * size)
    ja.right(180)
    ja.forward(100 * size)
    ja.left(90)
    ja.forward(15 * size)
    ja.right(90)
    i: int = 0
    while i < 180:
        ja.forward(size)
        ja.left(2)
        i += 1
    ja.penup()
    bubbles(x + 80 * size, y + 250 * size, size / 2)
    ja.pendown()


def fish(x: float, y: float, size: float) -> None:
    """Makes a fish."""
    assert size <= 1
    ja.penup()
    ja.goto(x, y)
    ja.pendown()
    ja.color("black")

    ja.begin_fill()
    ja.left(90)
    j: int = 0
    q: int = 0
    while j < 3:
        while q < 120:
            if j == 1:
                ja.right(3)
                ja.forward(size)
                q += 3
            else:
                ja.right(1)
                ja.forward(size)
                q += 1
        q = 0
        j += 1
    ja.right(180)
    ja.forward(60 * size)
    ja.left(90)
    ja.end_fill()


def bubbles(x: float, y: float, size: float) -> None:
    """BUBBLES!!!"""
    assert size <= 1
    ja.penup()
    ja.goto(x, y)
    ja.pendown()
    ja.color(99, 204, 250)

    r: int = 0
    k: int = 3
    while k > 0:
        while r < 360:
            ja.forward(size / k)
            ja.left(1)
            r += 1
        ja.penup()
        ja.left(90)
        ja.forward(150 * size / k)
        ja.right(90)
        ja.pendown()
        k -= 1
        r = 0


def main() -> None:
    """Idk, I was told to make all of this into a main function..."""
    f: int = 0
    while f < 2:
        stick_figure(randint(-350, 200), randint(-350, 200), randint(1, 10) / 10)
        fish(randint(-350, 250), randint(-350, 300), randint(1, 10) / 10)
        f += 1


if __name__ == "__main__":
    main()


ja.hideturtle()

done()