from utils import color_text, RED, GREEN, get_movie_name
from movie_storage import get_movies
import random


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



def search_movie():
    """
    Loads the information from the JSON file.
    Displays all movies which hold at least a substring of the movie name.
    """
    movies = get_movies()
    movie = get_movie_name().casefold()

    found = False
    for movies, details in movies.items():
        if movie in movies.casefold():
                print(color_text(f"- {movies}: {details["rating"]}", GREEN))
                found = True
    if not found:
        print(color_text("No entry under this name", RED))