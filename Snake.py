import time
from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()

    def add_segment(self, position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segment.append(tim)

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def grow(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seq in range(len(self.segment) - 1, 0, -1):
            x = self.segment[seq - 1].xcor()
            y = self.segment[seq - 1].ycor()
            self.segment[seq].goto(x, y)
        self.segment[0].forward(MOVE)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)