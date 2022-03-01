"""Learning about turtles!"""

from turtle import Turtle, colormode, done
colormode(255)

side_length: float = 300

leo: Turtle = Turtle()

leo.color(99, 204, 250)
leo.speed(5)

leo.penup()
leo.goto(-150, -60)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()

leo.hideturtle()

# Bob
bob: Turtle = Turtle()

bob.color(0, 0, 0)
bob.speed(50)

bob.penup()
bob.goto(-150, -60)
bob.pendown()

i: int = 0
while (i < 150):
    bob.forward(side_length)
    bob.left(121)
    i = i + 1
    side_length = side_length * 0.97

bob.hideturtle()

done()