import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter Colour:")
print(user_bet)
colours = ["red", "green", "blue", "purple", "orange", "yellow"]
Y_pos = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtle = []

for turtle_ind in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colours[turtle_ind])
    tim.penup()
    tim.goto(x=-240, y=Y_pos[turtle_ind])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You have won! {winning_colour} is the winning turtle.")
            else :
                print(f"You have lost! {winning_colour} is the winning turtle.")


        random_dist = random.randint(1, 10)
        turtle.forward(random_dist)

screen.exitonclick()
