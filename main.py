import random
import turtle
from turtle import Turtle,Screen

spiro = Turtle()

spiro.speed("fastest")
turtle.colormode(255)
spiro.pensize(3)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for _ in range(36):
    spiro.color(random_color())
    spiro.circle(100)
    spiro.setheading(spiro.heading() + 10)





screen = Screen()
screen.exitonclick()