from turtle import Turtle, Screen
from random import randint

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed(8)
t.width(7)


def random_colour():
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    return [r, g, b]


def random_step():
    direction = randint(1, 4)
    angle = 90 * direction
    t.setheading(angle)
    t.forward(50)


for _ in range(0, 50):
    rgb = random_colour()
    t.color(rgb[0], rgb[1], rgb[2])
    random_step()


screen.exitonclick()
