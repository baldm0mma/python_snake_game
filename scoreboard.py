from turtle import Turtle

# Constants
COLOR = "white"
ALIGNMENT = "center"
FONT = ("Fira Code", 12, "normal")
SCORE = 0
NAME = "Player"


class Scoreboard(Turtle):
    def __init__(self, screen_height, player_name=NAME, color=COLOR, starting_score=SCORE):
        super().__init__()
        self.starting_score = starting_score
        self.score = starting_score
        self.high_score = 0
        self.name = player_name
        self.color(color)
        self.penup()
        self.goto(0, (screen_height / 2 - 30))
        self.hideturtle()
        self.update_message()

    def update_score(self, new_score):
        self.score = new_score
        self.update_message()

    def update_message(self):
        self.clear()
        self.write(
            f"Score: {self.score} | {self.name}'s High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_message()
