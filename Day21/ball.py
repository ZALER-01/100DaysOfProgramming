from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # x_move and y_move determine the speed and diagonal direction
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1 # Used for time.sleep() inside the main loop

    def move(self):
        """Moves the ball diagonally by adding to the current X and Y positions."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Reverses the Y direction when hitting the top or bottom walls."""
        self.y_move *= -1

    def bounce_x(self):
        """Reverses the X direction when hitting a paddle and speeds up the ball."""
        self.x_move *= -1
        self.move_speed *= 0.9 # Multiplying by less than 1 decreases the sleep delay, making it faster

    def reset_position(self):
        """Resets ball to the center, resets speed, and serves to the opposite side."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x() # Inverts the direction so the serve goes to the player who just scored
