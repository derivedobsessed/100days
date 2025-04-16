from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        snake_length = len(self.segments)
        for i in reversed(range(1, snake_length)):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].setposition(x=new_x, y=new_y)
        self.head.forward(MOVE)
