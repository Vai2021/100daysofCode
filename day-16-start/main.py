# import turtle
# from turtle import Turtle, Screen
#
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclic

from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("pockemon name",["pikachu","squirtle","charmender"])
table.add_column("Type",["Electric","Water","fire"])
print(table.align)
table.align = "r"
print(table)