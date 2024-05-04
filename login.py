
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame

from review import *

from frames import *

from main import MainFrame

from register import Register

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / 'assets/login'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class LoginFrame(Frame):
    def __init__(self, app_frames):
        super().__init__(app_frames.master, bg="#FFFFFF")
        self.app_frames = app_frames
        self.setup_ui()
        self.entry_1.bind("<FocusIn>", self.on_username_entry_click)
        self.entry_1.bind("<FocusOut>", self.on_username_entry_focusout)
        self.entry_2.bind("<FocusIn>", self.on_password_entry_click)
        self.entry_2.bind("<FocusOut>", self.on_password_entry_focusout)

    def setup_ui(self):
        print(relative_to_assets("image_1"))
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 1080,
            width = 1920,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1920.0,
            1080.0,
            fill="#597B58",
            outline="")

        self.canvas.create_rectangle(
            68.0,
            0.0,
            1853.0,
            1080.0,
            fill="#87AF86",
            outline="")

        self.canvas.create_text(
            108.0,
            15,
            anchor="nw",
            text="Login",
            fill="#FFFFFF",
            font=("Koulen Regular", 128 * -1)
        )

        self.login_check = self.canvas.create_text(
            1380.25,
            520,
            anchor="center",
            text="",
            fill="#FFFFFF",
            font=("Koulen Regular", 30 * -1),
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            1381.0,
            594.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=1213.0,
            y=566.0,
            width=336.0,
            height=54.0
        )
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        #self.entry_image_2 = PhotoImage(
        #    file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            1381.0,
            672.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
        )
        self.entry_2.place(
            x=1213.0,
            y=644.0,
            width=336.0,
            height=54.0
        )

        self.button_1 = Button (
            bg="#586c4c",
            fg="#FFFFFF",
            text = "Login",
            font=("Koulen Regular", 30 * -1),
            activebackground="#586c4c",
            activeforeground="#586c4c",
            relief="flat",
            highlightthickness=0,
            borderwidth=0.5,
            command=lambda: self.login()
        )

        self.button_1.place (
            x = 1280.0,
            y = 723.0,
            width = 201.0,
            height = 51.0
        )

        self.button_2 = Button (
            bg="#586c4c",
            fg="#FFFFFF",
            text = "Sign Up",
            font=("Koulen Regular", 30 * -1),
            activebackground="#586c4c",
            activeforeground="#586c4c",
            relief="flat",
            highlightthickness=0,
            borderwidth=0.5,
            command=lambda: self.app_frames.switch_frame(Register)
        )

        self.button_2.place (
            x=1280.0,
            y=792.0,
            width=201.0,
            height=51.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            1381.0,
            279.0,
            image=self.image_image_1
        )

        self.entry_1.insert(0,"Enter Username")
        self.entry_2.insert(0,"Enter Password")

    def login(self):

        username = self.entry_1.get()
        password = self.entry_2.get()

        print("Username: " + username + "\nPassword: " + password)

        if self.app_frames.verify_user(username, password):
            print("Correct Login")
            self.app_frames.switch_frame(MainFrame)

        else:
            self.canvas.itemconfig(
                self.login_check, 
                text="Incorrect Username or Password",
                fill="#ff292c"
                )
            
    def on_password_entry_click(self, event):
        '''
        Password Focus: Removes the enter password text when the user clicks on the box

        Parameters: 
        event: The event object representing the FocusIn event.
        '''
        if self.entry_2.get() == "Enter Password":
            self.entry_2.delete(0, "end")
            self.entry_2.config(fg = 'black', show="*")

    def on_password_entry_focusout(self, event):
        '''
        Password Focus out: Reinserts the Enter Password text when the user clicks out of the password textbox

        Parameters: 
        event: The event object representing the FocusOut event.
        '''
        if not self.entry_2.get():
            self.entry_2.insert(0, "Enter Password")
            self.entry_2.config(fg = 'black', show="")

    def on_username_entry_click(self, event):
        '''
        Username Focus in: Removes the enter username text when the user clicks on the box

        Parameters: 
        event: The event object representing the FocusIn event.
        '''
        if self.entry_1.get() == "Enter Username":
            self.entry_1.delete(0, "end")
            self.entry_1.config(fg = 'black')

    def on_username_entry_focusout(self, event):
        '''
        Username Focus out: Reinserts the Enter Username text when the user clicks out of the username textbox

        Parameters: 
        event: The event object representing the FocusOut event.
        '''
        if not self.entry_1.get():
            self.entry_1.insert(0, "Enter Username")
            self.entry_1.config(fg = 'black')
