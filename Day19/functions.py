from turtle import *

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim_heading = tim.heading()  + 10
    tim.setheading(tim_heading)

def turn_right():
    tim_heading = tim.heading() -10
    tim.setheading(tim_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()




