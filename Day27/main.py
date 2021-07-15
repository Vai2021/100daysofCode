# import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI project")
window.minsize(width=500, height=300)

my_lable = Label(text="I am vaidehee", font=("Arial", 24, "bold"))
my_lable.pack()

my_lable["text"] = "New text"
my_lable.config(text="New text")


def button_clicked():
    print("I got clicked")
    my_lable.config(text="move forward")


button = Button(text ="click me", command="button_clicked")
button.pack()





window.mainloop()
