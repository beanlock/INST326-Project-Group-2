from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame
from pathlib import Path
from frames import *

class Register(Frame):
    def __init__(self, app_frames):
        super().__init__(app_frames.master)
        self.app_frames = app_frames
        self.configure(bg='white')
        self.setup_ui()
    
    def setup_ui(self):
        ASSETS_PATH = Path(__file__).parent / Path("assets/register")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            self,
            bg = "#87AF86",
            height = 1080,
            width = 1920,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            960.0,
            563.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=786.0,
            y=540.0,
            width=348.0,
            height=45.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            960.0,
            734.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=786.0,
            y=711.0,
            width=348.0,
            height=45.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            960.0,
            301.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1920.0,
            120.0,
            fill="#677F5B",
            outline="")

        self.canvas.create_text(
            960.0,
            500.0,
            anchor="center",
            text="Create your Username",
            fill="#FFFFFF",
            font=("Koulen Regular", 30 * -1)
        )

        self.canvas.create_text(
            960.0,
            675.0,
            anchor="center",
            text="Create your Password",
            fill="#FFFFFF",
            font=("Koulen Regular", 30 * -1)
        )

        self.button_1 = Button(
            bg="#586c4c",
            fg="#FFFFFF",
            text = "Register",
            font=("Koulen Regular", 30 * -1),
            activebackground="#586c4c",
            activeforeground="#586c4c",
            highlightthickness=0,
            borderwidth=0.5,
            command= self.register_user,
            relief="flat"
        )
        self.button_1.place(
            x=771.0,
            y=785.0,
            width=378.0,
            height=65.0
        )

        self.button_2 = Button(
            bg="#586c4c",
            fg="#FFFFFF",
            text = "Back to Login",
            font=("Koulen Regular", 30 * -1),
            activebackground="#586c4c",
            activeforeground="#586c4c",
            highlightthickness=0,
            borderwidth=0.5,
            command=lambda: self.app_frames.switch_frame(login.LoginFrame),
            relief="flat"
        )
        self.button_2.place(
            x=771.0,
            y=880.0,
            width=378.0,
            height=65.0
        )

        self.canvas.create_text(
            960.0,
            50.0,
            anchor="center",
            text="Register Your ReView account",
            fill="#FFFFFF",
            font=("Koulen Regular", 48 * -1)
        )
    def register_user(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        success = self.app_frames.register(username, password)
        if success:
            print("R")
