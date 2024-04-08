
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label

import review


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / 'assets/login'


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1920.0,
    1080.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    216.0,
    137.0,
    1480.0,
    842.0,
    fill="#87AF86",
    outline="")

canvas.create_text(
    264.0,
    161.0,
    anchor="nw",
    text="ReView Login",
    fill="#FFFFFF",
    font=("InriaSans Regular", 96 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1269.0,
    544.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1101.0,
    y=516.0,
    width=336.0,
    height=54.0
)
entry_1.insert(0,"Enter Username")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1269.0,
    622.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1101.0,
    y=594.0,
    width=336.0,
    height=54.0
)
entry_2.insert(0,"Enter Password")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login(),
    relief="flat"
)
button_1.place(
    x=1151.0,
    y=663.0,
    width=236.0,
    height=71.0
)

canvas.create_text(
    1222.0,
    672.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("InriaSans Regular", 36 * -1)
)

def login():
    username = entry_1.get()
    password = entry_2.get()

    print("Username: " + username + "\nPassword: " + password)

    label = Label(window, text = username + password)
    label.pack()

window.resizable(True, True)
window.mainloop()
