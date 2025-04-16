from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food("purple")
scoreboard = Scoreboard()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
screen.listen()

game_is_on = True
while game_is_on:
    snake.move()
    scoreboard.write(f"Score: {scoreboard.score}", align='left', font=('Arial', 20, 'normal'))
    # Eat food
    if snake.head.distance(food) <= 15:
        scoreboard.clear()
        scoreboard.add_point()
        snake.add_segment()
        scoreboard.write(f"Score: {scoreboard.score}", align='left', font=('Arial', 20, 'normal'))
        on_snake = True
        while on_snake:
            food.change_position()
            on_snake = False
            for segment in snake.segments:
                if segment.distance(food) <= 15:
                    on_snake = True
    # Detect wall
    if -280 > snake.head.xcor() or snake.head.xcor() > 280 or -280 > snake.head.ycor() or snake.head.ycor() > 280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collisions with your tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()


    screen.update()
    time.sleep(0.1)
screen.exitonclick()
