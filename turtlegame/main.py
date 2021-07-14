from turtle import Turtle
from turtle import Screen

timmy = Turtle()
timmy.shape("turtle")
# for i in range (4):
#     timmy.forward(100)
#     timmy.left(90)
# my_timmy_turtle.forward(100)
# my_timmy_turtle.left(90)
# my_timmy_turtle.forward(100)
# my_timmy_turtle.left(90)
# my_timmy_turtle.forward(100)
n=10
length = 270
for i in range (n):
    timmy.forward(length/n)
    timmy.penup()
    timmy.forward(length/n)
    timmy.pendown()















screen = Screen()
screen.exitonclick()

