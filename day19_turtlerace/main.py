import turtle as t
from random import randint

screen = t.Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a colour:')

red = t.Turtle(shape='turtle')
red.color('red')
red.penup()
red.setposition(x=-230, y=-125)

orange = t.Turtle(shape='turtle')
orange.color('orange')
orange.penup()
orange.setposition(x=-230, y=-75)

yellow = t.Turtle(shape='turtle')
yellow.color('yellow')
yellow.penup()
yellow.setposition(x=-230, y=-25)

green = t.Turtle(shape='turtle')
green.color('green')
green.penup()
green.setposition(x=-230, y=25)

blue = t.Turtle(shape='turtle')
blue.color('blue')
blue.penup()
blue.setposition(x=-230, y=75)


purple = t.Turtle(shape='turtle')
purple.color('purple')
purple.penup()
purple.setposition(x=-230, y=125)

turtles = [red, orange, yellow, green, blue, purple]

end = True
while end:
    for turtle in turtles:
        turtle.forward(randint(0, 15))
        if turtle.xcor() >= 230:
            end = False
            winner = turtle

if winner.color()[0] == user_bet.lower():
    print('You won!')
else:
     print(f'You lost. The {winner.color()[0]} turtle got there first')


screen.exitonclick()
