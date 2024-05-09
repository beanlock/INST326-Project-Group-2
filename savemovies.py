from imdb import Cinemagoer
import pickle


ia = Cinemagoer()
top_movies_list = ia.get_top250_movies()
top_details_list = []


for movie in top_movies_list:
    movie_id = movie.movieID
    movie_details = ia.get_movie(movie_id)
    

    ia.update(movie_details, info=['genres', 'release date', 'title', 'full-size cover url', 'plot'])
    
    top_details_list.append(movie_details)
    print(movie_details['title'])
    print("Genres:", movie_details.get('genres', ['N/A']))
    print("Release Year:", movie_details.get('year', 'N/A'))
    print("HD Cover Image:", movie_details.get('full-size cover url', 'N/A'))
    print("Plot:", movie_details.get('plot', 'N/A'))


with open('top_movies.pkl', 'wb') as f:
    pickle.dump(top_details_list, f)

print("Finished pickling")
