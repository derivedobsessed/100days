from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-40, 270)
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
    def add_point(self):
        self.score +=1
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 20, 'normal'))


