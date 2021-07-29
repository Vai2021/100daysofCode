from tkinter import *
from PIL import Image
from PIL import ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")

canvas = Canvas(width=200, height=224)
tomato_img = ImageTk.PhotoImage(Image.open("tomato.png"))
canvas.create_image(103, 112, image=tomato_img)
canvas.pack()

window.mainloop()
