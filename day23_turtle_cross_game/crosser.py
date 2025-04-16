from turtle import Turtle
STARTING_POSITION = (0, -250)
class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(STARTING_POSITION)
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shape("turtle")

    def up(self):
        new_y = self.ycor() + 10
        self.goto((self.xcor(), new_y))

    def start_over(self):
        self.goto(STARTING_POSITION)
