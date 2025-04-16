from turtle import Turtle
import time

class Puc(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.x_move = 10
        self.y_move = 10
        self.move_time = 0.1

    def bounce_x(self):
        self.move_time *= 0.7
        self.x_move = -self.x_move

    def bounce_y(self):
        self.y_move = -self.y_move

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto((new_x, new_y))

    def reset(self):
        super().goto(0, 0)
        self.bounce_x()
        self.move_time = 0.1


