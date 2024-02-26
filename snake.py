from turtle import Turtle

STARTING_SIZE = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in range(0, STARTING_SIZE):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.speed(10)
            new_segment.penup()
            new_segment.backward(segment * 20)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.speed(10)
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def head_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def head_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
