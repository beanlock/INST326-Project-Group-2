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
        self.register_check = self.canvas.create_text(
            960.0,
            520,
            anchor="center",
            text="",
            fill="#FFFFFF",
            font=("Koulen Regular", 30 * -1),
        )

        self.canvas.create_rectangle(
            113.0,
            211.0,
            590.0,
            841.0,
            fill="#67805C",
            outline="")

        self.button_states = {}

        self.profile_image_1 = PhotoImage(
            file=relative_to_assets("profile_1.png"))
        self.profile_1 = Button(
            image=self.profile_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.profile_1),
            relief="flat"
        )
        self.profile_1.place(
            x=170.0,
            y=361.0,
            width=165.0,
            height=165.0
        )
        self.button_states[self.profile_1] = False

        self.profile_image_2 = PhotoImage(
            file=relative_to_assets("profile_2.png"))
        self.profile_2 = Button(
            image=self.profile_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.profile_2),
            relief="flat"
        )
        self.profile_2.place(
            x=367.0,
            y=361.0,
            width=165.0,
            height=165.0
        )
        self.button_states[self.profile_2] = False

        self.profile_image_3 = PhotoImage(
            file=relative_to_assets("profile_3.png"))
        self.profile_3 = Button(
            image=self.profile_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.profile_3),
            relief="flat"
        )
        self.profile_3.place(
            x=367.0,
            y=553.0,
            width=165.0,
            height=165.0
        )
        self.button_states[self.profile_3] = False

        self.profile_image_4 = PhotoImage(
            file=relative_to_assets("profile_4.png"))
        self.profile_4 = Button(
            image=self.profile_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.profile_4),
            relief="flat"
        )
        self.profile_4.place(
            x=170.0,
            y=553.0,
            width=165.0,
            height=165.0
        )
        self.button_states[self.profile_4] = False

        self.canvas.create_text(
            350.0,
            280.0,
            anchor="center",
            text="Pick Your Avatar",
            fill="#FFFFFF",
            font=("Koulen Regular", 48 * -1)
        )

    def toggle(self, selected_profile):
        print(f"selected_profile: {selected_profile}, value: {self.button_states[selected_profile]}")

        for profile in self.button_states:
            if profile == selected_profile:
                self.button_states[profile] = not self.button_states[profile] 
                if self.button_states[profile]:
                    selected_profile.config(borderwidth=10, relief='solid')
                else:
                    selected_profile.config(borderwidth=0,  relief='flat')
            else:
                profile.config(borderwidth=0, relief='flat')
                self.button_states[profile] = False


        """
        for profile in self.button_states:
            if profile != selected_profile:
                profile.config(borderwidth=0, relief = 'flat')
                self.button_states[profile] = False


        if self.button_states[selected_profile] == True:
            selected_profile.config(borderwidth=0, relief ='flat')
            self.button_states[selected_profile] = False
        else:
            selected_profile.config(borderwidth=10, relief ='solid')
            self.button_states[selected_profile] = True
        """

    def register_user(self):
        username = self.entry_1.get()
        password = self.entry_2.get()
        

        success, user = self.app_frames.users.register_user(username, password)
        self.app_frames.current_user = user
        if success:
            print("Registration Successful Successful")

            i = 1
            print(f"{self.button_states.keys()}, {self.button_states.values()}")
            for button in self.button_states.values():
                if not button:
                    i+= 1
                else:
                    print(f"User profile set to #{i}")
                    user.profile=i
            try:
                user.profile
            except Exception as e:
                user.profile = 5

            self.app_frames.switch_frame(login.LoginFrame)
        else:
            self.canvas.itemconfig(
                self.register_check, 
                text="Incorrect Username or Password",
                fill="#ff292c"
                )
        
