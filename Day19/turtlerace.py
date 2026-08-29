import random
from turtle import Turtle, Screen

# Screen Setup
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")

# User Bet
user_bet = screen.textinput(
    title="Make Your Bet",
    prompt="Which turtle will win the race? Enter a colour:\n(red, green, blue, yellow, cyan, magenta)"
)

colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []
is_race_on = False

# Create Turtles
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])

    all_turtles.append(new_turtle)

# Start Race
if user_bet:
    is_race_on = True

# Result Writer
result = Turtle()
result.hideturtle()
result.penup()

while is_race_on:

    for turtle in all_turtles:

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        # Check Winner
        if turtle.xcor() >= 230:
            is_race_on = False

            winning_colour = turtle.pencolor()

            result.goto(-120, 150)

            if winning_colour.lower() == user_bet.lower():
                result.write(
                    f"You Won! {winning_colour.title()} Turtle Wins!",
                    font=("Arial", 16, "bold")
                )
            else:
                result.write(
                    f"You Lost! {winning_colour.title()} Turtle Wins!",
                    font=("Arial", 16, "bold")
                )

            print(f"The winner is {winning_colour}")

screen.exitonclick()
