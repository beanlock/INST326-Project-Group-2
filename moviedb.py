from imdb import Cinemagoer
from imdb import helpers
import tkinter as tk
import urllib as ul

ia = Cinemagoer()

#movies = ia.search_movie('the matrix reloaded')


movie = ia.get_movie("0133093")
#print(movie.current_info)
print(movie.infoset2keys)
#print(movie["genres"])
#print(movie["plot"])

#print(movie['full-size cover url'])

