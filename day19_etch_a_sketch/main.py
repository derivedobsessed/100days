import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def anti_clock():
    tim.left(10)


def clock():
    tim.right(10)


def clear_drawing():
    tim.clear()
    tim.home()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=anti_clock, key='a')
screen.onkey(fun=clock, key='d')
screen.onkey(fun=clear_drawing, key='c')
screen.exitonclick()
