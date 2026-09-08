from turtle import Screen


class GameScreen:
    def __init__(self):
        # Fetch the singleton Screen instance
        self.screen = Screen()

        # Configure window settings
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong")
        self.screen.tracer(0)

    def update(self):
        """Helper method to refresh the display frame."""
        self.screen.update()

    def listen(self):
        """Helper method to activate key listening."""
        self.screen.listen()

    def onkey(self, function, key):
        """Helper method to bind controls."""
        self.screen.onkey(function, key)

    def exit_on_click(self):
        """Helper method to close the window securely."""
        self.screen.exitonclick()
