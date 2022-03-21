from turtle import Turtle

# Constants
COLOR = "white"
ALIGNMENT = "center"
FONT = ("Fira Code", 12, "normal")
MESSAGE = "Score: "
SCORE = 0


class Scoreboard(Turtle):
    def __init__(self, screen_height, color=COLOR, message=MESSAGE, starting_score=SCORE):
        super().__init__()
        self.starting_score = starting_score
        self.score = starting_score
        self.color(color)
        self.penup()
        self.goto(0, (screen_height / 2 - 30))
        self.hideturtle()
        self.message = message
        self.update_message()

    def update_score(self, new_score):
        self.score = new_score
        self.clear()
        self.update_message()

    def update_message(self):
        self.write(f"{self.message}{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
