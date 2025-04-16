from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        with open("../../Desktop/data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", False, 'left', ('Ariel', 12, 'normal'))

    def start_over(self):
        self.clear()
        self.score = 0

    def add_point(self):
        self.score += 1
        new_score = self.score
        high_score = self.high_score
        if high_score < new_score:
            self.high_score = new_score
            with open("../../Desktop/data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

    def update_high_score(self):
        with open("../../Desktop/data.txt", mode="r") as file:
            self.high_score = int(file.read())
