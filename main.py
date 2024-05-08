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
        # Clear existing widgets
        for widget in self.winfo_children():
            widget.destroy()
        num_columns = 4
        num_rows = (len(recommended_movies) + num_columns - 1) // num_columns
        # Display new recommendations
        for index, movie in enumerate(recommended_movies):
            title = movie.get('title', 'Unknown Title')
            cover_url = movie.get('full-size cover url', '')

            row = index // num_columns
            column = index % num_columns 

            recommendation_frame = Frame(self, background="#67805C")
            recommendation_frame.grid(row=row, column=column, padx=10, pady=10)

            # Create a label for movie title
            title_label = Label(recommendation_frame, text=title, font=("Helvetica", 12), fg="#ffffff", bg="#67805C")
            title_label.pack()

            # Load movie cover image from URL and create a label
            if cover_url:
                # Fetch image from URL using requests
                response = requests.get(cover_url)
                image_data = response.content

                # Open image using Pillow
                image = Image.open(BytesIO(image_data))

                # Resize image if necessary
                max_width = 200  # Adjust as needed
                max_height = 200  # Adjust as needed
                image.thumbnail((max_width, max_height))

                # Convert image to Tkinter PhotoImage
                cover_image = ImageTk.PhotoImage(image)

                # Create label to display image
                cover_label = Label(recommendation_frame, image=cover_image)
                cover_label.image = cover_image  # To prevent garbage collection
                cover_label.pack()



        self.update_idletasks()  # Ensure GUI updates immediately


        """
            # Create a label for movie title
            title_label = Label(self, text=title, font=("Koulen", 12))
            title_label.grid(row=index, column=0, padx=10, pady=10)

            # Load movie cover image from URL
            if cover_url:
                # Fetch image from URL using requests
                response = requests.get(cover_url)
                image_data = response.content

                # Open image using Pillow
                image = Image.open(BytesIO(image_data))

                # Resize image if necessary
                max_width = 200  # Adjust as needed
                max_height = 200  # Adjust as needed
                image.thumbnail((max_width, max_height))

                # Convert image to Tkinter PhotoImage
                cover_image = ImageTk.PhotoImage(image)

                # Create label to display image
                cover_label = Label(self, image=cover_image)
                cover_label.image = cover_image  # To prevent garbage collection
                cover_label.grid(row=index, column=col + 1, padx=10, pady=10)
        
        # Add back button
        back_button = Button(
            self,
            text="Back to Login",
            command=lambda: self.app_frames.switch_frame(login.LoginFrame)
        )
        back_button.grid(row=len(recommended_movies), column=0, columnspan=2, pady=10)

        self.update_idletasks()  # Ensure GUI updates immediately
        """

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
