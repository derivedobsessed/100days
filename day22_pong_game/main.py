from turtle import Screen
from paddle import Paddle
from puc import Puc
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
screen.onkey(key='w', fun=l_paddle.up)
screen.onkey(key='s', fun=l_paddle.down)
screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)
screen.listen()
puc = Puc()

l_score = Score((-50, 250))
r_score = Score((50, 250))


game_is_on = True
while game_is_on:
    time.sleep(puc.move_time)
    puc.move()
    l_score.write(f"{l_paddle.score}", align='left', font=('Arial', 20, 'normal'))
    r_score.write(f"{r_paddle.score}", align='left', font=('Arial', 20, 'normal'))
    if puc.ycor() > 280 or puc.ycor() < -280:
        puc.bounce_y()

    if puc.distance(r_paddle) < 50 and puc.xcor() > 335 or puc.distance(l_paddle) < 50 and puc.xcor() < -335:
        puc.bounce_x()

    if puc.xcor() > 395:
        l_paddle.add_point()
        l_score.clear()
        puc.reset()

    if puc.xcor() < -395:
        r_paddle.add_point()
        r_score.clear()
        puc.reset()

    screen.update()

screen.exitonclick()
