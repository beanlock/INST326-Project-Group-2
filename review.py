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
        movietitle = ia.get_movie(self.movieID)["title"]
        print("Review of " + movietitle)
        print(maindb.users[self.ownerID].username + ": " + self.text)
        print("Rating: " + "★" * self.rating + "☆" * (10-self.rating))
    
    def __str__(self) -> str:
        return("Owner Id: " + self.ownerID + " Movie ID: " + self.movieID + " Rating: " + str(self.rating) + " Review Text: "+ self.text)

class User():
    """
    """
    def __init__(self, username, password):
        self.userID = generate_userID(maindb)
        self.username = username
        self.password = password
        self.watchlist = {}
        self.favorites = {}
        self.reviews = {}
        self.friends = {}
        self.reviewcount = 0
        maindb.users[self.userID] = self

    def create_review(self, movieID, rating, text):
        reviewID = str(self.reviewcount) + self.userID
        review = Review(reviewID, self.userID, movieID, rating, text)
        self.reviews[reviewID] = review
        self.reviewcount+= 1

    def display_all_reviews(self):
        for review in self.reviews.values():
            review.display_review()

#database of all users, keeps track of user objects and IDs
class UserDB():
    def __init__(self):
        self.used_ids = set()
        self.users = {}

    def is_id_used(self, userID):
        return userID in self.used_ids
    
    def add_user_id(self, userID):
        self.used_ids.add(userID)

maindb = UserDB()

#makes sure user id is unique
def generate_userID(db):
    while True:
        user_id = str(random.randint(0, 9999))
        if not db.is_id_used(user_id):
            db.add_user_id(user_id)
            return user_id

ia = Cinemagoer()

def main():
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

