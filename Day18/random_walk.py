import random
import turtle as t

t.colormode(255)

tim = t.Turtle()
tim.pensize(14)
tim.speed("fastest")

directions = [0, 90, 180, 270]

def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

for _ in range(200):
    tim.color(random_color())
    tim.forward(random.randint(10, 30))
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
