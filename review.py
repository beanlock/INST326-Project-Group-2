import random
from imdb import Cinemagoer
import pickle
import pytest


class Review():
    """
    A class to represent a user's review of a movie.

    Attributes:
    reviewID (str): ID composed from userID plus number of reviews.
    ownerID (str): ID of the person who left the review.
    movieID (str): IMDb ID of the movie being reviewed.
    rating (int): Rating of the movie from 1 to 10.
    text (str): Text of the review written by the user.
    """
    def __init__(self, reviewID, ownerID, movieID, rating, text):
        self.reviewID = reviewID 
        self.ownerID = ownerID
        self.movieID = movieID
        self.rating = rating
        self.text = text

    def display_review(self):
        """
        Prints the review with the movie title, username of the reviewer, review text, and star rating.
        """
        #retrieve the movie title using the imdb ID and ia.get_movie function
        movietitle = ia.get_movie(self.movieID)["title"]
        print("Review of " + movietitle)
        print(maindb.users[self.ownerID].username + ": " + self.text)
        print("Rating: " + "★" * self.rating + "☆" * (10-self.rating))
    
    def __str__(self) -> str:
        return("Owner Id: " + self.ownerID + " Movie ID: " + self.movieID + " Rating: " + str(self.rating) + " Review Text: "+ self.text)




class User():
    """
    A class to handle user activities such as creating and managing reviews and movie preferences.

    Attributes:
    userID (str): Unique ID to identify users.
    username (str): Unique username.
    password (str): Password for user authentication.
    reviews (dict): Dictionary of reviews, where the reviewID is the key, and the Review object is the value.
    watchlist (dict): List of movies saved by the user.
    favorites (dict): User's favorite movies (not yet implemented).
    friends (dict): User's friends (not yet implemented).
    reviewcount (int): Count of reviews made by the user.
    genre_preferences (dict): User's preferred genres with scores.
    
    """
    def __init__(self, username, password, user_db):
        if not maindb.is_username_used(username):
            #make sure username is not already taken 
            self.userID = generate_userID(maindb)
            self.username = username
            self.password = password
            self.reviews = {}
            self.watchlist = {}
            self.favorites = {}
            self.friends = {}
            self.reviewcount = 0
            user_db.add_user(self)
            user_db.users[self.userID] = self
            self.genre_preferences = {}
            print(f"{username} and {password} has been created")

    def __repr__(self) -> str:
        return f"User: {self.username}, Pass: {self.password}, UserID: {self.userID}, Genre Preferences: {self.genre_preferences}"
    

    def create_review(self, movieID, rating, text):
        """
        Creates a new review and adds it to the user's list of reviews.

        Args:
        movieID (str): The IMDb ID of the movie being reviewed.
        rating (int): The user's rating of the movie.
        text (str): The user's review text.
        """
        reviewID = str(self.reviewcount) + self.userID
        review = Review(reviewID, self.userID, movieID, rating, text)
        self.reviews[reviewID] = review
        self.reviewcount+= 1

        if rating >= 7:
            genres = ia.get_movie(movieID)["genres"]
            for genre in genres:
                if genre in self.genre_preferences:
                    self.genre_preferences[genre] += 1
                else:
                    self.genre_preferences[genre] = 1
        return reviewID

    def favorite_genres(self):
        """
        Returns the top three favorite genres of the user.

        Returns:
        list: Top three genres based on user preferences.
        """
        sorted_genres = sorted(self.genre_preferences, key=self.genre_preferences.get, reverse=True)
        return sorted_genres[:3]  #Returns top 3 genres
    
    def reviewed_movie_ids(self):
        movieIDS = []
        for review in self.reviews:
            movieIDS.append(review.movieID)

    def display_all_reviews(self):
        """
        Displays all reviews made by the user.
        """
        for review in self.reviews.values():
            review.display_review()

    def add_friend(self, user):
    
        self.friends[user.userID] = user

    def add_to_watchlist(self, movie_details):
        self.watchlist[movie_details["title"]] = movie_details
    #214
    def add_genres(self, genres):
        for genre in genres:
            self.genre_preferences[genre] += 5
        



class RecommendationEngine:
    def __init__(self, user):
        self.user = user

    def recommend(self):
        """
        Create a list of 10 movies based on genres that are highly rated from a user.

        Returns: 
        recommended_movies(list): 10 movie titles of reccomended movies
        (in the future this will probably return movie IDs instead of titles)
        """
        
        with open('top_movies.pkl', 'rb') as f:
            top_movies_list = pickle.load(f)

        favorite_genres = self.user.favorite_genres()
        recommended_movies = []
        
        for movie_details in top_movies_list:
            if 'genres' in movie_details:  
                if any(genre in movie_details['genres'] for genre in favorite_genres):
                    recommended_movies.append(movie_details)
                    print("Added " + str(movie_details['title']) + " to the list") 
                    if len(recommended_movies) >= 10:
                        break
        
        print("Tried to recommend")
        print(recommended_movies)
        return recommended_movies
        
        """
        favorite_genres = self.user.favorite_genres()
        for genre in favorite_genres:
            print(genre)
        recommended_movies = []
        
        #print(topmovies)
        for movie in top_movies_list:
            #movie_id = movie.movieID
            #print("movie id: " +  str(movie_id))
            #movie_details = ia.get_movie(movie_id)
            #print("Movie details: " + str(movie_details))
            if any(genre in movie_details['genres'] for genre in favorite_genres):
                recommended_movies.append(movie_details['title'])
                print("Added "+  str(movie_details['title']) + " to the list") 
            if(len(recommended_movies)>10):
                break
        print("tried to recommend")
        print(recommended_movies)
        return recommended_movies
        """
        
        

        """for movie in self.movies:
            movie_genres = set(ia.get_movie(movie.movieID)["genres"])  
            if movie_genres.intersection(favorite_genres) and movie.movieID not in self.user.reviewed_movie_ids():
                recommended_movies.append(movie)
        return recommended_movies
        """

#database of all users, keeps track of user objects and IDs
class UserDB():
    """
    Contains the database of users with their ID's and usernames that are all unique in order to avoid duplicates

    Attributes: 
    used_ids (set): A set of all user ID's to prevent repetition 
    used_usernames (set): A set of used usernames to prevent repetition
    users (dict): A dictionary of user objects, with the key being username
    """
    def __init__(self):
        self.used_ids = set()
        self.used_usernames = set()
        self.users = {}

    def is_id_used(self, userID):
        """
        Checks if userID is already used
        """
        return userID in self.used_ids
    
    def is_username_used(self, username):
        """
        Checks is username already used
        """
        return username in self.used_usernames
    
    def add_user_id(self, userID):
        """
        Marks userID as used
        """
        self.used_ids.add(userID)
    
    def add_user(self, user):
        self.users[user.username] = user
        self.add_user_id(user.userID)

    def verify_user(self, username, password):
        print(f"verifying {username} with pass {password}")
        print(self.users)
        user = self.users.get(username)
        print("user is supposed to be HEY LOOK HERE:" + str(user))
        if user and user.password == password:
            return (True, user)
        return (False, None)
    
    def register_user(self, username, password):
        if self.is_username_used(username):
            return False
        new_user = User(username, password, self)
        #self.users[new_user.userID] = new_user
        #self.used_usernames.add(username)
        self.users[username] = new_user
        return (True, new_user)

maindb = UserDB()

#makes sure user id is unique
def generate_userID(db):
    """
    Creates unique userID for new user

    Args:
    db (UserDB): The User database instance to check for existing ID's

    Returns:
    str: A unique userID
    """
    while True:
        user_id = str(random.randint(0, 9999))
        if not db.is_id_used(user_id):
            db.add_user_id(user_id)
            return user_id

ia = Cinemagoer('http')

def main():
    """
    A example of creating a user, searching for a movie and creating a review 
    """
    #testdb = UserDB()
    #topmovies = ia.get_top250_indian_movies()
    #print(topmovies)
    
    with open('top_movies.pkl', 'rb') as f:
            top_movies_list = pickle.load(f)
    for movie in top_movies_list:
        print(movie['genres'])
    """
    movies = ia.search_movie("spiderverse")
    #print(movies[:3])
    movie = movies[0]
    ia.update(movie)
    print(movie.infoset2keys)
    movieID = movie["imdbID"]
    testuser.create_review(movieID, 9, "this movie was really cool and good i liked it a lot")
    testuser.display_all_reviews()
    testReccomender = RecommendationEngine(testuser)
    reccomended_movies = testReccomender.recommend()
    for movie in reccomended_movies:
        print("Reccomended: " + str(movie))
    #testreview = Review("123", "0133093", 5, "wow this movie is really cool")
    #print(testreview)
    #testreview.display_review()
    """


def test_Review():
    testdb = UserDB()
    assert testdb.users == {}
    assert testdb.used_ids == set()
    assert testdb.used_usernames == set()

    testuser = User("beanlock", "brung", testdb)
    print(testdb.used_ids)
    assert testuser.userID in testdb.used_ids
    assert testuser.username == 'beanlock'
    assert testuser.password == 'brung'
    assert testuser.reviews == {}
    movies = ia.search_movie("spiderverse")
    #print(movies[:3])
    movie = movies[0]
    ia.update(movie)
    #print(movie.infoset2keys)
    movieID = movie["imdbID"]
    reviewID = testuser.create_review(movieID, 9, "this movie was really cool and good i liked it a lot")
    print(testuser.genre_preferences)
    assert testuser.genre_preferences == {'Animation': 1, 'Action': 1, 'Adventure': 1, 'Fantasy': 1, 'Sci-Fi': 1}
    assert testuser.reviews[reviewID].ownerID in testdb.used_ids
    assert testuser.reviews[reviewID].movieID == movieID
    assert testuser.reviews[reviewID].rating == 9
    #testuser.display_all_reviews()
    testRecommender = RecommendationEngine(testuser)
    recommended_movies = testRecommender.recommend()
    movietitles = []
    for movie in recommended_movies:
        movietitles.append(movie['title'])
    
    assert movietitles == ['The Dark Knight', 
                           'The Lord of the Rings: The Return of the King', 
                           'The Lord of the Rings: The Fellowship of the Ring', 
                           'The Good, the Bad and the Ugly', 
                           'The Lord of the Rings: The Two Towers', 
                           'Inception', 
                           'Star Wars: Episode V - The Empire Strikes Back', 
                           'The Matrix', 
                           'Interstellar', 
                           'Dune: Part Two']    
    
    login_attempt = testdb.verify_user('beanlock', 'brung')
    print(login_attempt)
    assert login_attempt == (True, testuser)
    register_attempt = testdb.register_user('deadshotguy', 'officerboles')
    print(register_attempt)
    assert register_attempt == (True, testdb.users.get('deadshotguy'))
    #testreview = Review("123", "0133093", 5, "wow this movie is really cool")
    #testreview.display_review()
    

if __name__ == "__main__":
    test_Review()
    main()
    

