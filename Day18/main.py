import random
from turtle import *
from random import *
import heroes


print(heroes.gen())

tim = Turtle()
# tim.shape("turtle")
# tim.color("blue")
# tim.forward(100)
# tim.backward(100)
# tim.left(90)
# screen = Screen()
# screen.exitonclick()

# for color coding we can use CS111 Website 
#TODO:1 Draw a square

# for _ in range(4):
#     tim.shape("turtle")
#     tim.forward(100)
#     tim.right(90)
    
#if we have imported simply turtle then we can use turtle.forward() instead of tim.forward() and turtle.right() instead of tim.right()
#modulename.nameOfclass()
# FROM MODULE NAME IMPORT CLASSNAME
tom = Turtle()
terry = Turtle()
#We can import everything by using astreak 
#We can use alias name

# for _ in range (15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
import random  # Fixes the NameError for random.choice
import turtle



colours = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]


def draw_shape(num_of_side):
    angle = 360 / num_of_side
    for _ in range(num_of_side):
        tim.forward(100)
        tim.right(angle)


# Loop automatically draws shapes from 3 sides (triangle) up to 10 sides (decagon)
for shape_side in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side)

turtle.done()  # Keeps the window open when finished


