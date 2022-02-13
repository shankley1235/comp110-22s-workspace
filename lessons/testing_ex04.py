"""Testing stuff."""

from random import randint
from turtle import Turtle, colormode, done
colormode(255)


def draw_circle(x_turtle: Turtle, radius: float, angle: float) -> None:
    x_turtle.setheading(-90)
    x_turtle.circle(radius, angle)


def draw_rectangle(x_turtle: Turtle, x: float, y: float, length: float, width: float) -> None:
    i: int = 0
    x_turtle.hideturtle()
    x_turtle.speed(0)
    x_turtle.penup()
    x_turtle.goto(x, y)
    x_turtle.pendown()
    x_turtle.color(217, 227, 98)
    x_turtle.begin_fill()
    while i < 4:
        x_turtle.forward(length)
        x_turtle.right(90)
        x_turtle.forward(width)
        i += 1
    x_turtle.end_fill()


ground: Turtle = Turtle()
draw_rectangle(ground, -760, -350, 1520, 50)


def draw_between_coord(x_turtle: Turtle, x: float, y: float) -> None:
    x_turtle.hideturtle()
    x_turtle.pendown()
    x_turtle.goto(x, y)
    x_turtle.penup()


def draw_waves(a_turtle: Turtle, radius: float, degrees: float, n: int) -> None:
    i: int = 0
    while i < n:
        a_turtle.setheading(-90)
        a_turtle.circle(radius, degrees)
        i += 1


def draw_ocean(a_turtle: Turtle, x: float, y: float) -> None:
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.begin_fill()
    a_turtle.color(14, 31, 237)
    a_turtle.pensize(3)
    a_turtle.pendown()
    draw_waves(a_turtle, 50, 180, 16)
    a_turtle.color(14, 237, 230)
    draw_between_coord(a_turtle, 800, -350)
    draw_between_coord(a_turtle, -800, -350)
    draw_between_coord(a_turtle, -800, 100)
    a_turtle.end_fill()
    

def draw_sky(a_turtle: Turtle, x: float, y: float) -> None:
    a_turtle.hideturtle()
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.pensize(0)
    a_turtle.color(219, 244, 242)
    draw_waves(a_turtle, 50, 180, 16)
    draw_between_coord(a_turtle, 800, 400)
    draw_between_coord(a_turtle, -800, 400)
    draw_between_coord(a_turtle, -800, 100)
    a_turtle.end_fill()


water: Turtle = Turtle()
draw_ocean(water, -800, 100)


air: Turtle = Turtle()
draw_sky(air, -800, 100)


def draw_sun(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    a_turtle.speed(0)
    a_turtle.hideturtle()
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.setheading(72)
    a_turtle.color("red")
    i: int = 0
    while i < 5:
        a_turtle.forward(side_length)
        a_turtle.right(144)
        i += 1
    i = 0
    a_turtle.begin_fill()
    while i < 300:
        if randint(1, 2) == 1:
            a_turtle.pencolor("red")
        else:
            a_turtle.pencolor("yellow")
        a_turtle.forward(side_length)
        a_turtle.right(144.25)
        i += 1
    a_turtle.fillcolor("yellow")
    a_turtle.end_fill()
    

sunshine: Turtle = Turtle()
draw_sun(sunshine, 500, 150, 200)


def random_color_fish(x_turtle: Turtle) -> None:
    if randint(1, 3) == 1:
        x_turtle.color(255, 255, 77)
    elif randint(1, 3) == 2:
        x_turtle.color(128, 0, 0)
    else:
        x_turtle.color(255, 0, 255)


def draw_fishy(x_turtle: Turtle, x: float, y: float, radius: float) -> None:
    x_turtle.speed(0)
    x_turtle.hideturtle()
    x_turtle.penup()
    x_turtle.goto(x, y)
    x_turtle.pendown()
    x_turtle.setheading(0)
    random_color_fish(x_turtle)
    x_turtle.begin_fill()
    x_turtle.circle(radius, 180)
    x_turtle.setheading(210)
    x_turtle.forward(radius * 4)
    x_turtle.setheading(90)
    x_turtle.forward(2 * radius)
    x_turtle.setheading(-30)
    x_turtle.forward(radius * 4)
    x_turtle.end_fill()
    x_turtle.penup()
    x_turtle.color("black")
    x_turtle.setheading(90)
    x_turtle.forward(1.3 * radius)
    x_turtle.pendown()
    x_turtle.begin_fill()
    x_turtle.circle(0.2 * radius, 360)
    x_turtle.end_fill()
    

fishy: Turtle = Turtle()
draw_fishy(fishy, -450, -150, randint(20, 50))
draw_fishy(fishy, 450, -150, randint(20, 50))
draw_fishy(fishy, -20, -330, randint(20, 50))
draw_fishy(fishy, 600, -300, randint(20, 50))

done()