import pickle

# load pickled movies from file
with open('top_movies.pkl', 'rb') as f:
    top_movies_list = pickle.load(f)

for movie in top_movies_list:
    print(movie['year'])
    print(movie['title'])
    print(movie['genres'])
    print(movie['full-size cover url'])