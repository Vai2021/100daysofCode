from turtle import Turtle
from turtle import Screen
import random

t = Turtle()
screen = Screen()

# t.colormode(255)


#
colours = ["CornflowerBlue", "DarkOrchid","Red","Yellow","Pink","Orange",
           "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

t.speed("fastest")
t.pensize(5)


def draw_spirograph(size_shape):
    for _ in range(int(360 / size_shape)):
        t.color(random.choice(colours))
        t.circle(100)
        t.setheading(t.heading() + 10)
        t.circle(100)


draw_spirograph(5)


screen.exitonclick()
