from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
import login
import main
import review
from review import UserDB, RecommendationEngine, Review, User
from imdb import Cinemagoer
from PIL import Image, ImageTk
import requests
from io import BytesIO


class AppFrames:
    """
     This class manages the frames of the application and user interactions.
    
    Attributes:
        master (Tk): The main window for the application.
        current_frame (Frame): The currently active frame.
        users (UserDB): A database handler for user operations.
        current_user (User): The currently logged-in user, managed during runtime.
    
    Methods:
        verify_user: Check if the given username and password match a registered user.
        switch_frame: Switch the visible frame in the Tkinter window.
        register: Register a new user with username and password.
        set_genres: Update the genre preferences for the current user.
    """
    def __init__(self, master):
        """
         Initialize the AppFrames class with the main Tkinter window and set the login frame as the default.

        Args:
            master (Tk): The main window of the application.
        """
        self.master = master
        self.master.state('zoomed')
        self.current_frame = None
        self.users = UserDB()
        self.switch_frame(login.LoginFrame)
    
    def verify_user(self, username, password):
        """
         Verify a user's login credentials.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        return self.users.verify_user(username, password)
    
    def switch_frame(self, frame_class):
        """
         Switch the currently displayed frame in the Tkinter window.

        Args:
            frame_class (Frame): The new frame class to be displayed.
        """
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(
            fill='both',
            expand=True
        )
    
    def register(self, username, password):
        """
        Register a new user with a username and password.

        Args:
            username (str): The username for the new user.
            password (str): The password for the new user.

        Returns:
            bool: True if registration is successful, False otherwise.
        """
        print("registered a current user!")
        success, user = self.users.register_user(username,password)
        self.current_user = user
        return success
    
    def set_genres(self, genres):
        """
         Set the genre preferences for the current user based on a list of genres.

        Args:
            genres (list): A list of genre strings to be added to the user's preferences.
        """
        print("called set_genres with " + str(genres))
        for genre in genres:
            if (genre in self.current_user.genre_preferences):
                self.current_user.genre_preferences[genre] += 5
                print(f"genre in preferences, added 5 to {genre}")
            else:
                self.current_user.genre_preferences[genre] = 5
                print(f"genre not in preferences, initialized {genre} with 5")

    


if __name__ == "__main__":

    root = Tk()
    app = AppFrames(root)
    root.mainloop()

    """
    testrecommender = RecommendationEngine(demouser)
    movies = ia.search_movie("madame web")
    movie = movies[0]
    ia.update(movie)
    movieID = movie["imdbID"]
    demouser.create_review(movieID, 9, "this movie was really cool and good i liked it a lot")
    testReccomender = RecommendationEngine(demouser)
    reccomended_movies = testReccomender.recommend()
    for movie in reccomended_movies:
        print(movie)
    """

    """
    root = Tk()
    app = AppFrames(root)
    """

