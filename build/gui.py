
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mattb\OneDrive\Documents\GitHub\INST326-Project\build\assets\frame0")


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
    fill="#597B58",
    outline="")

canvas.create_rectangle(
    68.0,
    0.0,
    1853.0,
    1080.0,
    fill="#87AF86",
    outline="")

canvas.create_text(
    108.0,
    0.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("Koulen Regular", 128 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1381.0,
    594.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=1213.0,
    y=566.0,
    width=336.0,
    height=54.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1381.0,
    672.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=1213.0,
    y=644.0,
    width=336.0,
    height=54.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1280.0,
    y=723.0,
    width=201.0,
    height=51.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1280.0,
    y=792.0,
    width=201.0,
    height=51.0
)

canvas.create_text(
    1350.0,
    723.0,
    anchor="nw",
    text="Login",
    fill="#FFFFFF",
    font=("Koulen Regular", 30 * -1)
)

canvas.create_text(
    1283.0,
    792.0,
    anchor="nw",
    text="Sign Up",
    fill="#FFFFFF",
    font=("Koulen Regular", 30 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1381.0,
    279.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()