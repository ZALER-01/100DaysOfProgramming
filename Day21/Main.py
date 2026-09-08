import time
from screen_setup import GameScreen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Initialize the screen from your external file
game_screen = GameScreen()

# Initialize Game Objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Setup Controls via the managed screen object
game_screen.listen()
game_screen.onkey(r_paddle.go_up, "Up")
game_screen.onkey(r_paddle.go_down, "Down")
game_screen.onkey(l_paddle.go_up, "w")
game_screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    game_screen.update() # Refreshes through the screen object
    ball.move()

    # 1. Detect Collision with Top and Bottom Walls (Height is 600, so boundaries are +/- 300)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # 2. Detect Collision with Right and Left Paddles
    # Checks distance to paddle AND ensures the ball has crossed the paddle line (+/- 320)
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # 3. Detect if Right Paddle Misses (Left Player scores a point)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # 4. Detect if Left Paddle Misses (Right Player scores a point)
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

game_screen.exit_on_click()
