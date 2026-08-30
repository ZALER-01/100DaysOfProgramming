from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My Snake Game Creating on 30-08-2026")

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment1 = Turtle("square")

segments = []

for position in starting_position:
    newSegment = Turtle(shape="square")
    newSegment.color("white")
    newSegment.penup()
    newSegment.goto(position)
    segments.append(newSegment)

#if we want something happens continiously go with while loop4
gameIson = True
while gameIson:
    for segment in segments:
        segment.forward(20)

# segment1 = Turtle(shape="square")
# segment1.color("white")
# segment1.penup()

# segment2 = Turtle(shape="square")
# segment2.color("white")
# segment2.penup()
# segment2.goto(-20, 0)
#
# segment3 = Turtle(shape="square")
# segment3.color("white")
# segment3.penup()
# segment3.goto(-40, 0)

screen.exitonclick()