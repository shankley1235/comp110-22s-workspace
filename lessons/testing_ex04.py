"""Testing stuff."""

from random import randint
from turtle import Turtle, colormode, done
colormode(255)


def turtle_settings(a_turtle: Turtle, x: float, y: float) -> None:
    a_turtle.hideturtle()
    a_turtle.speed(2)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()


# def draw_rectangle(a_turtle: Turtle, x: float, y: float, length: float, width: float) -> None:
#     i: int = 0
#     turtle_settings(a_turtle, x, y)
#     a_turtle.color(217, 227, 98)
#     a_turtle.begin_fill()
#     while i < 4:
#         a_turtle.forward(length)
#         a_turtle.right(90)
#         a_turtle.forward(width)
#         i += 1
#     a_turtle.end_fill()


# ground: Turtle = Turtle()
# draw_rectangle(ground, -760, -350, 1520, 50)


# def draw_between_coord(x_turtle: Turtle, x: float, y: float) -> None:
#     x_turtle.speed(0)
#     x_turtle.hideturtle()
#     x_turtle.pendown()
#     x_turtle.goto(x, y)
#     x_turtle.penup()


# def draw_waves(a_turtle: Turtle, radius: float, degrees: float, n: int) -> None:
#     i: int = 0
#     while i < n:
#         a_turtle.setheading(-90)
#         a_turtle.circle(radius, degrees)
#         i += 1


# def draw_ocean(a_turtle: Turtle, x: float, y: float) -> None:
#     turtle_settings(a_turtle, x, y)
#     a_turtle.begin_fill()
#     a_turtle.color(14, 31, 237)
#     a_turtle.pensize(3)
#     draw_waves(a_turtle, 50, 180, 16)
#     a_turtle.color(14, 237, 230)
#     draw_between_coord(a_turtle, 800, -350)
#     draw_between_coord(a_turtle, -800, -350)
#     draw_between_coord(a_turtle, -800, 100)
#     a_turtle.end_fill()
    

# def draw_sky(a_turtle: Turtle, x: float, y: float) -> None:
#     turtle_settings(a_turtle, x, y)
#     a_turtle.begin_fill()
#     a_turtle.pensize(0)
#     a_turtle.color(219, 244, 242)
#     draw_waves(a_turtle, 50, 180, 16)
#     draw_between_coord(a_turtle, 800, 400)
#     draw_between_coord(a_turtle, -800, 400)
#     draw_between_coord(a_turtle, -800, 100)
#     a_turtle.end_fill()


# water: Turtle = Turtle()
# draw_ocean(water, -800, 100)


# air: Turtle = Turtle()
# draw_sky(air, -800, 100)


# def draw_star(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
#     turtle_settings(a_turtle, x, y)
#     a_turtle.color("yellow")
#     a_turtle.begin_fill()
#     i: int = 0
#     while i < 5:
#         a_turtle.forward(side_length)
#         a_turtle.right(144)
#         i += 1
#     a_turtle.end_fill()


# def draw_sun(a_turtle: Turtle, x: float, y: float, side_length: float) -> None:
#     turtle_settings(a_turtle, x, y)
#     a_turtle.setheading(72)
#     a_turtle.color("red")
#     i: int = 0
#     draw_star(a_turtle, x, y, side_length)
#     i = 0
#     a_turtle.begin_fill()
#     while i < 300:
#         if randint(1, 2) == 1:
#             a_turtle.pencolor("red")
#         else:
#             a_turtle.pencolor("yellow")
#         a_turtle.forward(side_length)
#         a_turtle.right(144.25)
#         i += 1
#     a_turtle.fillcolor("yellow")
#     a_turtle.end_fill()
    

sunshine: Turtle = Turtle()
# draw_sun(sunshine, 500, 150, 200)


# def draw_moon(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
#     turtle_settings(a_turtle, x, y)
#     a_turtle.begin_fill()
#     a_turtle.color(232, 232, 232)
#     a_turtle.circle(radius, 360)
#     a_turtle.end_fill()
#     a_turtle.setheading(90)
#     a_turtle.forward(radius)
#     a_turtle.color("black")
#     a_turtle.begin_fill()
#     a_turtle.circle(radius, 360)
#     a_turtle.end_fill()

# moon_shine: Turtle = Turtle()
# draw_moon(moon_shine, 500, 150, 100)


def random_color_fish(x_turtle: Turtle) -> None:
    if randint(1, 4) == 1:
        x_turtle.color(255, 255, 77)
    elif randint(1, 4) == 2:
        x_turtle.color(128, 0, 0)
    elif randint(1, 4) == 3:
        x_turtle.color(255, 0, 255)
    else:
        x_turtle.color("green")


def draw_fishy(a_turtle: Turtle, x: float, y: float, radius: float) -> None:
    turtle_settings(a_turtle, x, y)
    a_turtle.setheading(0)
    random_color_fish(a_turtle)
    a_turtle.begin_fill()
    a_turtle.circle(radius, 180)



    a_turtle.left(30)
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
    

fishy: Turtle = Turtle()
draw_fishy(fishy, -450, -150, randint(20, 50))
draw_fishy(fishy, 450, -150, randint(20, 50))
draw_fishy(fishy, -20, -330, randint(20, 50))
draw_fishy(fishy, 600, -300, randint(20, 50))


# def draw_cloud(a_turtle: Turtle, x: float, y: float, size: str) -> None:
#     turtle_settings(a_turtle, x, y)
#     a_turtle.color("white")
#     n: int = 0
#     if size == "small":
#         n = 2
#     if size == "medium":
#         n = 3
#     if size == "large":
#         n = 4
#     i: int = 0
#     while i < n:
#         a_turtle.begin_fill()
#         a_turtle.setheading(-90)
#         a_turtle.circle(40, 360)
#         a_turtle.end_fill()
#         a_turtle.setheading(0)
#         a_turtle.forward(70)
#         i += 1
#     a_turtle.penup()
#     a_turtle.goto(x + 40, y - 40)
#     i = 0
#     a_turtle.pendown()
#     while i < n - 1:
#         a_turtle.begin_fill()
#         a_turtle.setheading(-90)
#         a_turtle.circle(40, 360)
#         a_turtle.end_fill()
#         a_turtle.setheading(0)
#         a_turtle.forward(70)
#         i += 1


# cloud: Turtle = Turtle()
# draw_cloud(cloud, -460, 300, "large")
# draw_cloud(cloud, 0, 300, "medium")
# draw_cloud(cloud, -700, 350, "small")


done()