from random import randint
from turtle import Turtle

class Food(Turtle):
    def __init__(self, color):
        super().__init__()
        super().penup()
        super().goto(-50, -50)
        super().color(color)
        super().shape('circle')
        super().shapesize(0.5, 0.5)
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        super().goto(random_x, random_y)
    def change_position(self):
        new_x = randint(-280, 280)
        new_y = randint(-280, 280)
        super().goto(new_x, new_y)
