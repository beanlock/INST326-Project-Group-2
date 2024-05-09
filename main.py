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
    """
     MainFrame provides the primary user interface in the application once the user has logged in.
    It displays user profiles and movie recommendations.

    Attributes:
        app_frames (AppFrames): The controller of the main application frames.
    """
    def __init__(self, app_frames):
        """
          Initialize the MainFrame with the parent application frames.

        Args:
            app_frames (AppFrames): The controller of the main application frames.
        """
        super().__init__(app_frames.master)
        self.app_frames = app_frames
        self.configure(bg='#87af86')
        self.setup_ui()
    
    def setup_ui(self):
        """
        Set up the user interface of the main frame. This includes layout of buttons,
        profile images, and other UI components.
        """
        ASSETS_PATH = Path(__file__).parent / Path("assets/main")

        def relative_to_assets(path: str) -> Path:
            """
            Get the absolute path for a file located in the main frame's assets directory.

            Args:
                path (str): The relative path from the assets directory.

            Returns:
                Path: The absolute path computed from the base assets directory.
            """
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

        print(f"{self.app_frames.current_user.profile+1}")

        self.profile_image = Image.open(relative_to_assets(f"profile_{self.app_frames.current_user.profile}.png"))
        self.resized_image = self.profile_image.resize((120,120))
        self.tk_image = ImageTk.PhotoImage(self.resized_image)
        self.image_2 = self.canvas.create_image(
            1980.0-120,
            60.0,
            image=self.tk_image
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
            command=lambda: self.display_recommendations(self.generate_recommended_movies(self.app_frames.current_user)),
            relief="flat"
        )
        self.button_1.place(
            x=771.0,
            y=600.0,
            width=378.0,
            height=65.0
        )
        print(str(self.app_frames.current_user))
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
        """
        Display the recommended movies in a grid layout.

        Args:
            recommended_movies (list of dict): A list of recommended movie details including title and cover image URL.
        """

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



    def generate_recommended_movies(self, user):
        engine = RecommendationEngine(user)
        reclist = engine.recommend()
        return reclist
        

    

               

userdb = UserDB()

def generate_recommended_movies(user):
    engine = RecommendationEngine(user)
    reclist = engine.recommend()
    return reclist

    """
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
    """
