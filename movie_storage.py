import json
from utils import color_text, BLUE, RED, GREEN


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
    while True:
        movie = input(color_text("Enter movie name or 'X' to exit: ", BLUE)).title()
        if movie.lower() == "x":
            return
        if movie in movies:
            print(color_text(f"Movie '{movie}' already exists", RED))
            return

        rating = get_movie_rating()
        year = get_movie_year()

        while True:
            user_escape = input(color_text(f"Save the movie: '{movie} ({year}) - {rating} Y/N ?", GREEN))
            if user_escape.lower() not in ("n","y"):
                print(color_text("Enter Y/N", RED))
                continue
            if user_escape.lower() == "n":
                break
            if user_escape.lower() == "y":
                movies[movie] = {"rating": rating, "year": year}
                print(color_text(f"Movie '{movie}' successfully added", GREEN))
                save_movies(movies)
                break


def delete_movie(get_movie_name):
    """
    Deletes a movie from the movie database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    for title, details in movies.items():
        rating = details["rating"]
        year = details["year"]
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
                while True:
                    user_choice = input(color_text(f"Delete: {movie} ({year}) {rating} ? - Y/N", RED))
                    if user_choice == "":
                        print("Enter Y/N")
                        continue
                    if user_choice.lower() == "n":
                        return
                    if user_choice.lower() == "y":
                        del movies[movie]
                        print(color_text(f"Movie '{movie}' successfully deleted", GREEN))
                        save_movies(movies)
                        break
            return


def update_movie(get_movie_name, get_movie_rating):
    movies = get_movies()
    while True:
        movie = input(color_text("Enter movie name or 'X' to exit: ", BLUE)).title()
        if movie == "":
            print(color_text(f"Invalid Input. Enter a valid name", RED))
            continue
        if movie.lower() == "x":
            return

        if movie not in movies:
            print(color_text(f"Movie '{movie}' doesn't exist", RED))
            continue

        year = movies[movie]["year"]
        choice = input(color_text("Do you want to update the movie name? (Y/N): ", BLUE))

        while True:
            if choice.lower() not in ("y", "n"):
                print("Enter Y or N")
                choice = input(color_text("Do you want to update the movie name? (Y/N): ", BLUE))
                continue

            if choice.lower() == "y":
                new_name = get_movie_name()
                rating = get_movie_rating()
                # delete old entry, add new one
                del movies[movie]
                movies[new_name] = {"rating": rating, "year": year}
                print(color_text(f"Movie name and rating successfully updated to '{new_name}'", GREEN))
                break

            if choice.lower() == "n":
                rating = get_movie_rating()
                movies[movie] = {"rating": rating, "year": year}
                print(color_text(f"Rating for movie '{movie}' successfully updated", GREEN))
                break

        save_movies(movies)
        return
