from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle() # Hides the turtle arrow shape so only text shows
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous frame and redraws both scores in position."""
        self.clear()
        # Draw Left Player Score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # Draw Right Player Score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increases left player's score and refreshes the display."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increases right player's score and refreshes the display."""
        self.r_score += 1
        self.update_scoreboard()
