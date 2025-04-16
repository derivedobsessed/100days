
from turtle import Turtle, Screen

from random import randint

t = Turtle()
screen = Screen()
screen.colormode(255)

def random_colour():
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    return [r, g, b]

def draw(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for i in range(3, 11):
    rgb = random_colour()
    t.color(rgb[0], rgb[1], rgb[2])
    draw(i)


screen.exitonclick()

