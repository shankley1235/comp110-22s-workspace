"""A Day and Night at the Ocean."""

"""Break up complex functions (5 points total):"""
"""Lines: 58 - 69."""
"""I used my draw_ocean function to call my draw_waves and draw_between_coord functions to outline the waves as well as the borders of an ocean."""

"""Try something fun! (5 points total):"""
"""Lines: 99 - 117."""
"""I drew a lot of contiunous, stars with a slight rotation as well as a randomized side length color to give the impression of a sun with rays of light."""


_author__ = "730435749"


from turtle import Turtle, colormode, done
from random import randint
colormode(255)


def turtle_settings(a_turtle: Turtle, x: float, y: float) -> None:
    """Establishes the desired characteristics of each turtle while also moving it to the user's desired location."""
    a_turtle.hideturtle()
    a_turtle.speed(0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()


def draw_rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Draws rectangle of given length and width whose top-left corner is at x, y."""
    i: int = 0
    turtle_settings(a_turtle, x, y)
    a_turtle.color(217, 227, 98)
    a_turtle.begin_fill()
    while i < 4:
        a_turtle.forward(length)
        a_turtle.right(90)
        a_turtle.forward(width)
        i += 1
    a_turtle.end_fill()


def draw_between_coord(x_turtle: Turtle, x: float, y: float) -> None:
    """Forces the turtle to draw while being moved to a given x, y."""
    x_turtle.speed(0)
    x_turtle.hideturtle()
    x_turtle.pendown()
    x_turtle.goto(x, y)
    x_turtle.penup()


def draw_waves(a_turtle: Turtle, radius: float, degrees: float, n: int) -> None:
    """Uses a loop to draw a given number of adjacent, partial circles with an arbitrary radius and amount of degrees circulated."""
    i: int = 0
    while i < n:
        a_turtle.setheading(-90)
        a_turtle.circle(radius, degrees)
        i += 1


def draw_ocean(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws the waves on top of the ocean while also drawing its bottom, left, and right borders on the picture."""
    turtle_settings(a_turtle, x, y)
    a_turtle.begin_fill()
    a_turtle.color(14, 31, 237)
    a_turtle.pensize(3)
    draw_waves(a_turtle, 50, 180, 16)
    a_turtle.color(14, 237, 230)
    draw_between_coord(a_turtle, 800, -350)
    draw_between_coord(a_turtle, -800, -350)
    draw_between_coord(a_turtle, -800, 100)
    a_turtle.end_fill()


def draw_sky(a_turtle: Turtle, x: float, y: float) -> None:
    """Draws the top, left, right, and bottom borders of the sky. The bottom border can be drawn using the draw_waves function."""
    turtle_settings(a_turtle, x, y)
    a_turtle.begin_fill()
    a_turtle.pensize(0)
    draw_waves(a_turtle, 50, 180, 16)
    draw_between_coord(a_turtle, 800, 400)
    draw_between_coord(a_turtle, -800, 400)
    draw_between_coord(a_turtle, -800, 100)
    a_turtle.end_fill()


def draw_star(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """Draws a five-pointed star."""
    turtle_settings(a_turtle, x, y)
    a_turtle.color("yellow")
    a_turtle.begin_fill()
    i: int = 0
    while i < 5:
        a_turtle.forward(side_length)
        a_turtle.right(144)
        i += 1
    a_turtle.end_fill()


def draw_sun(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
    """Continuously draws five-pointed stars while both slightly rotating after each star as well as randomly choosing a color in between each side of a star."""
    turtle_settings(a_turtle, x, y)
    a_turtle.setheading(72)
    a_turtle.color("red")
    i: int = 0
    draw_star(a_turtle, x, y, side_length)
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


def draw_moon(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Draws two overlapping circles if different color to draw a crescent moon."""
    turtle_settings(a_turtle, x, y)
    a_turtle.begin_fill()
    a_turtle.color(232, 232, 232)
    a_turtle.circle(radius, 360)
    a_turtle.end_fill()
    a_turtle.setheading(90)
    a_turtle.forward(radius)
    a_turtle.color("black")
    a_turtle.begin_fill()
    a_turtle.circle(radius, 360)
    a_turtle.end_fill()


def random_color_fish(x_turtle: Turtle) -> None:
    """Uses a random number generator to randomly choose the color of each fish"""
    if randint(1, 4) == 1:
        x_turtle.color(255, 255, 77)
    elif randint(1, 4) == 2:
        x_turtle.color(128, 0, 0)
    elif randint(1, 4) == 3:
        x_turtle.color(255, 0, 255)
    else:
        x_turtle.color("green")


def draw_fishy(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    """Uses a semicircle paired with a diagonal, cross shape to draw a fish."""
    turtle_settings(a_turtle, x, y)
    a_turtle.setheading(0)
    random_color_fish(a_turtle)
    a_turtle.begin_fill()
    a_turtle.circle(radius, 180)
    a_turtle.setheading(210)
    a_turtle.forward(radius * 4)
    a_turtle.setheading(90)
    a_turtle.forward(2 * radius)
    a_turtle.setheading(-30)
    a_turtle.forward(radius * 4)
    a_turtle.end_fill()
    a_turtle.penup()
    a_turtle.color("black")
    a_turtle.setheading(90)
    a_turtle.forward(1.3 * radius)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(0.2 * radius, 360)
    a_turtle.end_fill()


def draw_cloud(a_turtle: Turtle, x: float, y: float, size: str) -> None:
    """Uses overlapping circles of the same color to draw a cloud. Also allows the user to determine the relative size of each cloud."""
    turtle_settings(a_turtle, x, y)
    a_turtle.color("white")
    n: int = 0
    if size == "small":
        n = 2
    if size == "medium":
        n = 3
    if size == "large":
        n = 4
    i: int = 0
    while i < n:
        a_turtle.begin_fill()
        a_turtle.setheading(-90)
        a_turtle.circle(40, 360)
        a_turtle.end_fill()
        a_turtle.setheading(0)
        a_turtle.forward(70)
        i += 1
    a_turtle.penup()
    a_turtle.goto(x + 40, y - 40)
    i = 0
    a_turtle.pendown()
    while i < n - 1:
        a_turtle.begin_fill()
        a_turtle.setheading(-90)
        a_turtle.circle(40, 360)
        a_turtle.end_fill()
        a_turtle.setheading(0)
        a_turtle.forward(70)
        i += 1


def main() -> None:
    """The entrypoint of my scene."""
    sand: Turtle = Turtle()
    water: Turtle = Turtle()
    air: Turtle = Turtle()
    fishy: Turtle = Turtle()
    light: Turtle = Turtle()
    sky_features: Turtle = Turtle()
    draw_rectangle(sand, -760, -350, 1520, 50)
    draw_ocean(water, -800, 100)
    draw_fishy(fishy, -450, -150, randint(20, 50))
    draw_fishy(fishy, 450, -150, randint(20, 50))
    draw_fishy(fishy, -20, -330, randint(20, 50))
    draw_fishy(fishy, 600, -300, randint(20, 50))
    if randint(0, 1) == 0:
        air.color("black")
        draw_sky(air, -800, 100)
        draw_moon(light, 500, 150, 100)
        draw_star(sky_features, -460, 300, 25)
        draw_star(sky_features, 0, 300, 40)
        draw_star(sky_features, -700, 350, 20) 
    else:
        air.color(219, 244, 242)
        draw_sky(air, -800, 100)
        draw_sun(light, 500, 150, 200)
        draw_cloud(sky_features, -460, 300, "large")
        draw_cloud(sky_features, 0, 300, "medium")
        draw_cloud(sky_features, -700, 350, "small")
    done()


if __name__ == "__main__":
    main()