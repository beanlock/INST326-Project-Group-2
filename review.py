import random
from imdb import Cinemagoer


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
        Prints the review with the the movie title the usseraname of the reviewer, the text of the review and the number of stars.
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
    password(str): NYI
    watchlist(dict): NYI
    favorites(dict): NYI
    friends(dict): NYI
    reviewcount(int): # of reviews made by the user
    
    """
    def __init__(self, username, password):
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
            maindb.users[self.userID] = self

    def create_review(self, movieID, rating, text):
        """
        Creates a new review and adds it to the sers list of reviews.

        Args:
        movie ID (str): The IMDB ID of the moving that is getting reviewed 
        rating (int): The users rating of the movie
        text (str): The users typed out review of the movie
        """
        reviewID = str(self.reviewcount) + self.userID
        review = Review(reviewID, self.userID, movieID, rating, text)
        self.reviews[reviewID] = review
        self.reviewcount+= 1

    def display_all_reviews(self):
        for review in self.reviews.values():
            review.display_review()

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

ia = Cinemagoer()

def main():
    """
    A example of creating a user, searching for a movie and creating a review 
    """
    testuser = User("beanlock", "brung")

    

    movies = ia.search_movie("spiderverse")
    #print(movies[:3])
    movie = movies[0]
    ia.update(movie)
    #print(movie.infoset2keys)
    movieID = movie["imdbID"]
    testuser.create_review(movieID, 9, "this movie was really cool and good i liked it a lot")
    testuser.display_all_reviews()

    #testreview = Review("123", "0133093", 5, "wow this movie is really cool")
    #print(testreview)
    #testreview.display_review()


if __name__ == "__main__":
    main()

