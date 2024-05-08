import tkinter as tk
from pathlib import Path
from frames import *

class Register(tk.Frame):
    def __init__(self, app_frames):
        super().__init__(app_frames.master)
        self.app_frames = app_frames
        self.configure(bg='white')

        self.button_1 = Button(
            bg="#586c4c",
            fg="#FFFFFF",
            text = "Register",
            font=("Koulen Regular", 30 * -1),
            activebackground="#586c4c",
            activeforeground="#586c4c",
            highlightthickness=0,
            borderwidth=0.5,
            command= self.,
            relief="flat"
        )
        self.button_1.place(
            x=771.0,
            y=785.0,
            width=378.0,
            height=65.0
        )



        