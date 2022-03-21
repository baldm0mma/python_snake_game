from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Welcome to Snake!")
screen.tracer(0)

# Game State
game_is_running = False

# Instances
snake = Snake()
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
scoreboard = Scoreboard(SCREEN_HEIGHT)

screen.update()
game_is_running = True

# Event listeners,key bindings, and movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# move snake
while game_is_running:
    head_x_cord = snake.head.xcor()
    head_y_cord = snake.head.ycor()

    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 7:
        food.refresh()
        snake.extend_tail()
        scoreboard.update_score(scoreboard.score + 1)

    # Detect collision with boundary
    if head_x_cord >= SCREEN_WIDTH / 2 - 10 or head_x_cord <= -(SCREEN_WIDTH / 2 - 10) or head_y_cord >= SCREEN_HEIGHT / 2 - 10 or head_y_cord <= -(SCREEN_HEIGHT / 2 - 10):
        game_is_running = False
        scoreboard.game_over()

    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 7:
            game_is_running = False
            scoreboard.game_over()


screen.exitonclick()
