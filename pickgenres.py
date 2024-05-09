from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame
from pathlib import Path
from frames import *
from main import MainFrame

class Genres(Frame):
    """
     A Frame that allows users to select their preferred movie genres in the application.

    Attributes:
        app_frames (AppFrames): The controller of the main application frames.
        genres (dict): Tracks which genres are selected with boolean values.
    """
    def __init__(self, app_frames):
        """
         Initialize the Genres frame with the parent application frames.

        Args:
            app_frames (AppFrames): The controller of the main application frames.
        """
        super().__init__(app_frames.master)
        self.app_frames = app_frames
        self.configure(bg='white')
        self.setup_ui()
        self.genres = {"Drama" : False, 
                       "Sci-Fi" : False, 
                       "Comedy" :  False, 
                       "Action" : False, 
                       "Romance" : False, 
                       "Adventure": False}

    def setup_ui(self):
        """
         Set up the user interface of the genre selection frame. This includes layout of buttons
        and other UI components to allow users to toggle their genre preferences.
        """
        ASSETS_PATH = Path(__file__).parent / Path("assets/genre")

        def relative_to_assets(path: str) -> Path:
            """
             Get the absolute path for a file located in the genre frame's assets directory.

            Args:
                path (str): The relative path from the assets directory.

            Returns:
                Path: The absolute path computed from the base assets directory.
            """
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
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1920.0,
            269.0,
            fill="#67805C",
            outline="")

        self.canvas.create_text(
            960.0,
            120.0,
            anchor="center",
            text="PICK YOUR GENRES",
            fill="#FFFFFF",
            font=("Koulen Regular", 96 * -1)
        )

        self.button_1 = Button(
            bg='#73708D',
            activebackground='#73708D',
            fg="#FFFFFF",
            text="Drama",
            font=("Koulen Regular", 30 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.button_1),
            relief="flat",
        )
        self.button_1.gray = '#73708D'
        self.button_1.color = '#645ADA'
        self.button_1.text = "Drama"
        
        self.button_1.place(
            x=283.0,
            y=334.0,
            width=244.0,
            height=440.0
        )

        self.button_2 = Button(
            bg='#A4A07D',
            activebackground='#A4A07D',
            fg="#FFFFFF",
            text="Sci-Fi",
            font=("Koulen Regular", 30 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.button_2),
            relief="flat"
            
        )
        self.button_2.place(
            x=971.0,
            y=334.0,
            width=262.0,
            height=440.0
        )
        self.button_2.gray = '#A4A07D'
        self.button_2.color = '#DCD16D'
        self.button_2.text = "Sci-Fi"

        self.button_3 = Button(
            bg='#5F7F92',
            activebackground='#5F7F92',
            fg="#FFFFFF",
            text="Comedy",
            font=("Koulen Regular", 30 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.button_3),
            relief="flat"
        )
        self.button_3.place(
            x=1265.0,
            y=566.0,
            width=380.0,
            height=208.0
        )
        self.button_3.gray = '#5F7F92'
        self.button_3.color = '#57A6D2'
        self.button_3.text = "Comedy"

        self.button_4 = Button(
            bg='#9E847F',
            activebackground='#9E847F',
            fg="#FFFFFF",
            text="Action",
            font=("Koulen Regular", 30 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.button_4),
            relief="flat"
        )
        self.button_4.place(
            x=559.0,
            y=334.0,
            width=379.0,
            height=208.0
        )
        self.button_4.gray = '#9E847F'
        self.button_4.color = '#F49A86'
        self.button_4.text = "Action"

        self.button_5 = Button(
            bg='#A17983',
            activebackground='#A17983',
            fg="#FFFFFF",
            text="Romance",
            font=("Koulen Regular", 30 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.button_5),
            relief="flat"
        )
        self.button_5.place(
            x=1265.0,
            y=334.0,
            width=380.0,
            height=214.0
        )
        self.button_5.gray = '#A17983'
        self.button_5.color = '#EA6E8C'
        self.button_5.text = "Romance"

        self.button_6 = Button(
            bg='#907F98',
            activebackground='#907F98',
            fg="#FFFFFF",
            text="Adventure",
            font=("Koulen Regular", 30 * -1),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.toggle(self.button_6),
            relief="flat"
        )
        self.button_6.place(
            x=559.0,
            y=560.0,
            width=379.0,
            height=214.0
        )
        self.button_6.gray = '#907F98'
        self.button_6.color = '#D293F0'
        self.button_6.text = "Adventure"

        self.button_7 = Button(
            bg="#586c4c",
            fg="#FFFFFF",
            text = "Done",
            font=("Koulen Regular", 30 * -1),
            activebackground="#586c4c",
            activeforeground="#586c4c",
            highlightthickness=0,
            borderwidth=0.5,
            command=lambda: self.submit_genres(),
            relief="flat"
        )
        self.button_7.place(
            x=810.0,
            y=860.0,
            width=300.0,
            height=100.0
        )

    def toggle(self, button):
        """
        Toggle the color and selection status of a genre button when clicked.

        Args:
            button (Button): The genre button to toggle.
        """
        current_color = button['bg']

        if current_color == button.gray:
            button.config(bg=button.color)
        else:
            button.config(bg=button.gray)

        if self.genres[button.text]:
            self.genres[button.text] = False
            print(f"{button.text} changed to false")
        else:
            self.genres[button.text] = True
            print(f"{button.text} changed to True")
    
    def submit_genres(self):
        """
        Submit the selected genres and switch to the main application frame if any genres are selected.
        """
        try:
            print("called submit_genres")
            selectedlist = []
            for genre, selected in self.genres.items():
                if selected:
                    print(f"added {genre} to the list")
                    selectedlist.append(genre)
            if len(selectedlist) == 0:
                return
            self.app_frames.set_genres(selectedlist)
            self.app_frames.switch_frame(MainFrame)
        except Exception as e:
            print("An error occurred:", e)


        
    



        