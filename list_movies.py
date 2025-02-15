from movie_storage import get_movies


def list_movies():
    """
    Lists all movies of the movie database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    for movie_name, details in movies.items():
        print(f"{movie_name} ({details["year"]}): {details["rating"]}")
