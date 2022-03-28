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
        self.high_score = int(self.read_previous_data("score"))
        self.high_score_player_name = self.read_previous_data("name")
        self.name = player_name
        self.color(color)
        self.penup()
        self.goto(0, (screen_height / 2 - 30))
        self.hideturtle()
        self.update_message()

    def read_previous_data(self, type):
        # note: the first line of the data.txt file is the plater name, the second is the high score.
        type = 0 if type == "name" else 1
        with open(file="./data.txt") as file:
            return file.read().splitlines()[type]

    def write_new_data(self):
        with open(file="./data.txt", mode="w") as file:
            file.write(f"{self.high_score_player_name}\n{self.high_score}")

    def update_score(self, new_score):
        self.score = new_score
        self.update_message()

    def update_message(self):
        self.clear()
        self.write(
            f"{self.name}'s Score: {self.score} | {self.high_score_player_name}'s High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score_player_name = self.name
            self.high_score = self.score
            self.write_new_data()
        self.score = 0
        self.update_message()
