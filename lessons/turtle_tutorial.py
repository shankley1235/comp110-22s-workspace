"""Turtle tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.begin_fill()

leo.speed(10)
leo.hideturtle()
leo.color("yellow", "yellow")
leo.penup()
leo.goto(-150, 129.9)
leo.pendown()

i: int = 0
side_length: float = 300
while i < 3:
    leo.forward(side_length)
    leo.right(90 + 30)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()

bob.color("black")
bob.speed(200)
bob.hideturtle()
bob.penup()
bob.goto(-150, 129.9)
bob.pendown()

i = 0

while i < 500:
    bob.forward(side_length)
    bob.right(120.5)
    side_length = side_length * 0.97
    i += 1

done()
