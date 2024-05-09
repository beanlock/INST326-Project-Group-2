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
    def __init__(self, master):
        self.master = master
        self.master.state('zoomed')
        self.current_frame = None
        self.users = UserDB()
        self.switch_frame(login.LoginFrame)
    
    def verify_user(self, username, password):
        return self.users.verify_user(username, password)
    
    def switch_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(
            fill='both',
            expand=True
        )
    
    def register(self, username, password):
        print("registered a current user!")
        success, user = self.users.register_user(username,password)
        self.current_user = user
        return success
    
    def set_genres(self, genres):
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

