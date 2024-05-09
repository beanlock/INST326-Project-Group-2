import random
from imdb import Cinemagoer
import pickle


class Review():
    """
    Review: a user's review of a movie

    Attributes:
    reviewID: ID composite from userID + # of reviews
    ownerID: ID of the person who left the review
    movieID: imdb ID of the movie being reviewed
    rating: 1-10 rating of the movie 
    text: Text of the review written by the user
    """
    def __init__(self, reviewID, ownerID, movieID, rating, text):
        self.reviewID = reviewID 
        self.ownerID = ownerID
        self.movieID = movieID
        self.rating = rating
        self.text = text

    def display_review(self):
        """
        Prints the review with the the movie title the useraname of the reviewer, the text of the review and the number of stars.
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
    User: Handles user creation and actions, like leaving reviews, displaying reviews, etc.

    Attributes:
    userID(str): unique ID to identify users
    username(str): unique username
    reviews(dict): dictionary of reviews, reviewID is the key, and review object is the value
    password(str): Password to log into the account
    watchlist(dict): List of movies and details saved by the user to watch
    friends(dict): NYI
    reviewcount(int): # of reviews made by the user
    
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
            #UserDB.users[self.userID] = self
            self.genre_preferences = {}
            print(f"{username} and {password} has been created")

    def __repr__(self) -> str:
        return f"User: {self.username}, Pass: {self.password}, UserID: {self.userID}, Genre Preferences: {self.genre_preferences}"
    

    def create_review(self, movieID, rating, text):
        """
        Creates a new review and adds it to the users list of reviews.

        Args:
        movie ID (str): The IMDB ID of the moving that is getting reviewed 
        rating (int): The users rating of the movie
        text (str): The users typed out review of the movie
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

    def favorite_genres(self):
        sorted_genres = sorted(self.genre_preferences, key=self.genre_preferences.get, reverse=True)
        return sorted_genres[:3]  #Returns top 3 genres
    
    def reviewed_movie_ids(self):
        movieIDS = []
        for review in self.reviews:
            movieIDS.append(review.movieID)

    def display_all_reviews(self):
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
        # Load pickled top movies list
        with open('top_movies.pkl', 'rb') as f:
            top_movies_list = pickle.load(f)

        favorite_genres = self.user.favorite_genres()
        recommended_movies = []
        
        for movie_details in top_movies_list:
            if 'genres' in movie_details:  # Check if genres information is available
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
    Contains the database of usees with thei ID's and usernames that are all different in order to avoid confusion

    Attributes: 
    used_ids (set): A set of all user ID's to prevent repatition 
    used_usernames (set): A set of used usernames to prevent repatition
    users (dict): A dictinoary of user objects, with the key bing userID
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
        self.users[user.userID] = user
    
    def verify_user(self, username, password):
        print(f"verifying {username} with pass {password}")
        print(self.users)
        user = self.users.get(username)
        print(user)
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
    str: A unuque userID
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
    #testuser = User("beanlock", "brung", testuser)
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

if __name__ == "__main__":
    main()

