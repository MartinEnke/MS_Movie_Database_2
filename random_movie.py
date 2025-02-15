from utils import color_text
from movie_storage import get_movies
import random

# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"


def random_movie():
    """
    Loads the information from the JSON file.
    Randomly picks and displays a movie from the database.
    """
    movies = get_movies()
    movies_list = []
    for movie in movies:
        movies_list.append(movie)
    movie = random.choice(movies_list)
    rating = movies[movie]["rating"]
    year = movies[movie]["year"]

    print(color_text(f"Your movie for tonight: '{movie} ({year})', Rating: {rating}", GREEN))