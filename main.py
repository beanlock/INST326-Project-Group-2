from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, Frame
from pathlib import Path
from frames import *
from review import UserDB, RecommendationEngine, Review, User
import login
from imdb import Cinemagoer
from PIL import Image, ImageTk
import requests
from io import BytesIO

class MainFrame(Frame):
    def __init__(self, app_frames):
        super().__init__(app_frames.master)
        self.app_frames = app_frames
        self.configure(bg='#87af86')
        self.setup_ui()
    
    def setup_ui(self):
        ASSETS_PATH = Path(__file__).parent / Path("assets/main")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            self,
            bg="#87AF86",
            height=1080,
            width=1920,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.pack(fill='both', expand=True)

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            960.0,
            562.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            master=self.canvas,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=680.0,
            y=531.0,
            width=560.0,
            height=60.0
        )

        self.entry_1.insert(0,"Type to start your ReView journey")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            960.0,
            286.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1920.0,
            120.0,
            fill="#677F5B",
            outline=""
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            1856.0,
            60.0,
            image=self.image_image_2
        )

        self.button_1 = Button(
            bg="#586c4c",
            fg="#FFFFFF",
            text = "ReCommend!",
            font=("Koulen Regular", 30 * -1),
            activebackground="#586c4c",
            activeforeground="#586c4c",
            highlightthickness=0,
            borderwidth=0.5,
            command=lambda: self.display_recommendations(generate_recommended_movies()),
            relief="flat"
        )
        self.button_1.place(
            x=771.0,
            y=600.0,
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

    def display_recommendations(self, recommended_movies):
        for widget in self.winfo_children():
            widget.destroy()
        num_columns = 4
        num_rows = (len(recommended_movies) + num_columns - 1) // num_columns
        for index, movie in enumerate(recommended_movies):
            title = movie.get('title', 'Unknown Title')
            cover_url = movie.get('full-size cover url', '')

            row = index // num_columns
            column = index % num_columns 

            recommendation_frame = Frame(self, background="#67805C")
            recommendation_frame.grid(row=row, column=column, padx=10, pady=10)


            title_label = Label(recommendation_frame, text=title, font=("Helvetica", 12), fg="#ffffff", bg="#67805C")
            title_label.pack()


            if cover_url:
                response = requests.get(cover_url)
                image_data = response.content

                image = Image.open(BytesIO(image_data))

                max_width = 200
                max_height = 200
                image.thumbnail((max_width, max_height))

                cover_image = ImageTk.PhotoImage(image)

                cover_label = Label(recommendation_frame, image=cover_image)
                cover_label.image = cover_image
                cover_label.pack()

        self.update_idletasks()

userdb = UserDB()

def generate_recommended_movies():
    ia = Cinemagoer()
    demouser = User("4x", "99", userdb)
    testrecommender = RecommendationEngine(demouser)
    movies = ia.search_movie("madame web")
    #print(movies[:3])
    movie = movies[0]
    ia.update(movie)
    #print(movie.infoset2keys)
    movieID = movie["imdbID"]
    demouser.create_review(movieID, 9, "this movie was really cool and good i liked it a lot")
    recommended_movies = testrecommender.recommend()
    for movie in recommended_movies:
        print("Reccomended: " + str(movie))
    return recommended_movies
