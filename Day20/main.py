import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialize Game Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for Keyboard Controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # 1. Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 2. Detect collision with wall boundaries
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        scoreboard.game_over()

    # 3. Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
