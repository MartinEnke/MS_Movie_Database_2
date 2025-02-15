from utils import color_text, get_movie_name
from movie_storage import get_movies

# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"


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