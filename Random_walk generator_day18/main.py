from turtle import Turtle
import random

t = Turtle()
t.pensize(10)
t.speed("fastest")
colours = ["CornflowerBlue", "DarkOrchid", "Pink",
           "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "Black", "Red"]
directions = [0, 90, 180, 270]


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colours = (r,g,b)
    return random_colours


for _ in range(300):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(directions))

# for _ in range(50):
#     t.color(random.choice(colours))
#     t.forward(20)
#     t.right(90)
#     t.forward(20)
#     t.left(90)
