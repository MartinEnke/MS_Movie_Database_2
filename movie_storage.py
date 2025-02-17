import json
from utils import color_text, get_movie_name, get_movie_rating, get_movie_year

# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"



def get_movies():
    """
    Returns a dictionary of dictionaries that contains the movies information.
    """
    with open("data.json", "r") as file:
        movies = json.load(file)
        return movies


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("data.json", "w") as file:
        json.dump(movies, file, indent=4)


def add_movie(get_movie_name, get_movie_rating, get_movie_year):
    """
    Adds a movie to the movie database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    movie = get_movie_name()
    for movie_name, details in movies.items():
            if movie in movie_name:
                print(color_text(f"Movie '{movie}' already exists", RED))
                return

    rating = get_movie_rating()
    year = get_movie_year()

    movies[movie] = {"rating": rating, "year": year}

    save_movies(movies)
    print(color_text(f"Movie '{movie}' successfully added", "32"))


def delete_movie(get_movie_name):
    """
    Deletes a movie from the movie database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    movie = get_movie_name()
    if movie in movies:
        del movies[movie]
        print(color_text(f"Movie '{movie}' successfully deleted", GREEN))
    else:
        print(color_text(f"Movie '{movie}' doesn't exist", RED))

    save_movies(movies)


def update_movie(get_movie_name, get_movie_rating):
    """
    Updates a movie from the movie database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    while True:
        movie = input(color_text("Enter movie name or 'X' to exit: ", BLUE)).title()
        if movie == "":
            print(color_text(f"Invalid Input. Enter a valid name", RED))
            continue
        if movie.lower() == "x":
            return

        if not movie in movies:
            print(color_text(f"Movie '{movie}' doesn't exist", RED))
            continue

        if movie in movies:
            year = movies[movie]["year"]
            choice = input(color_text("Do you want to edit the movie name Y/N ?" , BLUE))
            if choice.lower() == "y":
                movie = get_movie_name()
                rating = get_movie_rating()
                movies[movie] = {"rating": rating, "year": year}
            if choice.lower() == "n":
                rating = get_movie_rating()
                movies[movie] = {"rating": rating, "year": year}

        print(color_text(f"Movie '{movie}' successfully updated", GREEN))

        save_movies(movies)
        return