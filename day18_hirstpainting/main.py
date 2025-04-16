import turtle as t
from random import choice
width, height = 300, 300

tim = t.Turtle()
screen = t.Screen()
screen.setup(width + 20, height + 20)
tim.penup()
tim.pos()
tim.hideturtle()
tim.speed('fastest')
tim.goto(-width//2+10, -height//2+20)
screen.colormode(255)
colors = [(202, 172, 172), (222, 228, 228), (238, 245, 245), (153, 180, 180), (152, 186, 186), (193, 161, 161), (214, 204, 204), (208, 179, 179), (174, 188, 188), (161, 213, 213), (162, 203, 203), (114, 123, 123), (175, 161, 161), (214, 181, 181), (98, 98, 98), (44, 44, 44), (199, 208, 208), (98, 96, 96), (89, 92, 92), (20, 22, 22), (38, 36, 36), (105, 111, 111), (66, 63, 63), (66, 64, 64)]

for r in range(10):
    for c in range(9):
        tim.dot(10, choice(colors))
        tim.forward(30)
    tim.dot(10, choice(colors))
    tim.setheading(90)
    if r % 2 == 0:
        tim.forward(30)
        tim.left(90)
    else:
        tim.forward(30)
        tim.right(90)

screen.exitonclick()




