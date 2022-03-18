from turtle import Turtle
import random

# Constants
COLOR = "red"


class Food(Turtle):
    def __init__(self, screen_width, screen_height, color=COLOR):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.shape("circle")
        self.penup()
        self.color(color)
        self.speed("fastest")
        self.shapesize(stretch_wid=0.25, stretch_len=0.25)
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-(self.screen_width / 2 - 20),
                                    self.screen_width / 2 - 20, 10)
        random_y = random.randrange(-(self.screen_height / 2 - 20),
                                    self.screen_height / 2 - 20, 10)
        self.goto(x=random_x, y=random_y)
