from turtle import Turtle

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        super().penup()
        super().hideturtle()
        super().color("white")
        super().goto(position)
