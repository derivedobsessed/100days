from turtle import Turtle, Screen
from random import randint


t = Turtle()
screen = Screen()
screen.colormode(255)

def rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

for x in range(0, 100):
    angle = 360 / 100
    t.setheading(angle * x)
    t.color(rgb())
    t.circle(50)


#comment

t.speed('fastest')

screen.exitonclick()
