from utils import color_text
from movie_storage import get_movies

# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"


def movies_sorted_by_rating():
    """
    Loads the information from the JSON file.
    Converts the dictionary into two lists to display all movies sorted by their rating.
    """
    movies = get_movies()

    movie_names = []
    movie_ratings = []
    for movie, details in movies.items():
        movie_names.append(movie)
        movie_ratings.append(details["rating"])

    for i in range(len(movie_ratings)):
        for j in range(i + 1, len(movie_ratings)):
            # Compare ratings
            if movie_ratings[i] < movie_ratings[j]:
                # Swap ratings - if lower rating first
                movie_ratings[i], movie_ratings[j] = movie_ratings[j], movie_ratings[i]
                # Swap corresponding movie names
                movie_names[i], movie_names[j] = movie_names[j], movie_names[i]
    print(color_text(f"Movies listed by rating:", GREEN))
    for i in range(len(movie_names)):
        print(f"- {movie_names[i]}: {movie_ratings[i]}")


def movies_sorted_by_year():
    """
    Loads the information from the JSON file.
    Converts the dictionary into two lists to display all movies sorted by their year.
    """
    movies = get_movies()
    movie_names = []
    movie_years = []
    for movie, details in movies.items():
        movie_names.append(movie)
        movie_years.append(details["year"])

    for i in range(len(movie_years)):
        for j in range(i + 1, len(movie_years)):
            # Compare ratings
            if movie_years[i] < movie_years[j]:
                # Swap ratings - if lower rating first
                movie_years[i], movie_years[j] = movie_years[j], movie_years[i]
                # Swap corresponding movie names
                movie_names[i], movie_names[j] = movie_names[j], movie_names[i]
    print(color_text(f"Movies listed by rating:", GREEN))
    for i in range(len(movie_names)):
        print(f"- {movie_names[i]}: {movie_years[i]}")