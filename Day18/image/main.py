import turtle as t
import random

t.colormode(255)

color_list = [
    (239, 242, 247), (245, 240, 231), (246, 239, 244), (237, 245, 241),
    (200, 158, 118), (60, 96, 130), (148, 85, 58), (220, 208, 119),
    (136, 163, 187), (20, 34, 51), (187, 145, 159), (50, 26, 18),
    (123, 73, 91), (132, 177, 155), (56, 121, 76), (176, 160, 40),
    (56, 25, 35), (197, 94, 77), (129, 27, 41), (149, 24, 16),
    (20, 45, 36), (180, 96, 113), (224, 170, 189), (42, 61, 98),
    (65, 163, 101), (223, 177, 169), (108, 119, 164), (26, 90, 56),
    (156, 210, 189), (13, 86, 101)
]

tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Starting position
tim.setpos(-225, -225)

for row in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

    tim.setx(-225)
    tim.sety(tim.ycor() + 50)

screen = t.Screen()
screen.exitonclick()