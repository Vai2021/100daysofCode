from turtle import Turtle
from turtle import Screen
import random

t = Turtle()
t.pensize(8)
colour = ["magenta", "chocolate", "medium violet red", "chartreuse", "medium blue", "slate gray", "dark red",
          "light sky blue", "dark olive green","black"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for shape_side in range(3, 11):
    t.color(random.choice(colour))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()
