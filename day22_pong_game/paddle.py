from turtle import Turtle
MOVE = 30
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        super().goto(position)
        super().shape("square")
        super().shapesize(stretch_wid=1, stretch_len=5)
        super().color('white')
        super().setheading(90)
        super().penup()
        self.score = 0

    def up(self):
        super().setheading(UP)
        super().forward(MOVE)

    def down(self):
        super().setheading(DOWN)
        super().forward(MOVE)

    def add_point(self):
        self.score += 1

