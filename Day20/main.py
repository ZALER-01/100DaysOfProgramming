import time
from turtle import Turtle, Screen

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Starting positions for the 3 snake segments
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# Create and position each segment FIRST
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# Start the game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Move the body segments from back to front
    # Segment 3 moves to Segment 2's position, Segment 2 moves to Segment 1's position
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    # Move the head (Segment 0) forward
    segments[0].forward(20)

screen.exitonclick()
