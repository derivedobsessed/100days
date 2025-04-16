from turtle import Turtle
import random
COLORS = ["red", "green", "blue", "yellow", "orange", "pink"]


class Cars():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(0, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            random_y = random.randint(-200, 200)
            new_car.goto(-300, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() + 10
            car.goto(new_x, car.ycor())

