from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')

for i in range(0,30):
    tim.forward(10)
    tim.color('white')
    tim.forward(10)
    tim.color('black')

screen = Screen()
screen.exitonclick()


