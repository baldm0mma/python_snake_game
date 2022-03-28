from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVEMENT_DISTANCE = 10
UP_ANGLE = 90
DOWN_ANGLE = 270
LEFT_ANGLE = 180
RIGHT_ANGLE = 0
COLOR = "purple"


class Snake:
    def __init__(self, color=COLOR):
        self.color = color
        self.segments = self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        segments = []
        for position in STARTING_POSITIONS:
            new_segment = self.create_segment(position)
            segments.append(new_segment)
        return segments

    def create_segment(self, position):
        segment = Turtle("square")
        segment.color(self.color)
        segment.shapesize(.5, .5, 1)
        segment.penup()
        segment.goto(position)
        return segment

    def extend_tail(self):
        tail_position = self.segments[-1].position()
        new_segment = self.create_segment(tail_position)
        self.segments.append(new_segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            (prev_x, prev_y) = self.segments[segment - 1].position()
            self.segments[segment].goto(x=prev_x, y=prev_y)
        self.segments[0].forward(MOVEMENT_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN_ANGLE:
            self.head.setheading(UP_ANGLE)

    def down(self):
        if self.head.heading() != UP_ANGLE:
            self.head.setheading(DOWN_ANGLE)

    def left(self):
        if self.head.heading() != RIGHT_ANGLE:
            self.head.setheading(LEFT_ANGLE)

    def right(self):
        if self.head.heading() != LEFT_ANGLE:
            self.head.setheading(RIGHT_ANGLE)

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.segments = self.create_snake()
        self.head = self.segments[0]
