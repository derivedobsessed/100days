from turtle import Screen
from crosser import Crosser
from cars import Cars
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)
screen.listen()
screen.title("Crossing Game")

crossing_turtle = Crosser()
scoreboard = Scoreboard()

game_is_on = True

screen.onkey(crossing_turtle.up, "Up")
cars = Cars()


while game_is_on:
    scoreboard.update()
    time.sleep(0.1*(0.9**scoreboard.score))
    cars.create_car()
    cars.move()
    for car in cars.all_cars:
        if crossing_turtle.distance(car) < 20:
            scoreboard.start_over()
            crossing_turtle.start_over()
            scoreboard.update()

    if crossing_turtle.ycor() > 220:
        crossing_turtle.start_over()
        scoreboard.add_point()
        scoreboard.update_high_score()
        scoreboard.update()

    screen.update()

screen.exitonclick()
