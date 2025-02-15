from utils import color_text
from movie_storage import get_movies

# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"


def filtering_movies():
    """
    Loads the information from the JSON file.
    Filters the movies based on minimum rating, as well as start & end year requested from the user.
    """
    movies = get_movies()
    while True:
        min_rating = input(color_text(f"Enter minimum rating (leave blank for no minimum rating): ", BLUE))
        if min_rating == "":
            min_rating = 0.0
            break
        try:
            min_rating = float(min_rating)
            break
        except ValueError:
            print(color_text(f"Invalid input. Please enter a valid number.", RED))

    while True:
        start_year = input(color_text(f"Enter start year (leave blank for no start year): ", BLUE))
        if start_year == "":  # Allowing blank input
            start_year = 0
            break
        try:
            start_year = int(start_year)
            break
        except ValueError:
            print(color_text(f"Invalid input. Please enter a valid year.", RED))

    while True:
        end_year = input(color_text(f"Enter end year (leave blank for no end year): ", BLUE))
        if end_year == "":  # Allowing blank input
            end_year = 3000
            break
        try:
            end_year = int(end_year)
            break
        except ValueError:
            print(color_text(f"Invalid input. Please enter a valid year.", RED))

    filtered_by_rating = {}
    for movie, details in movies.items():
        if details["rating"] >= min_rating and start_year <= details["year"] and end_year >= details["year"]:
            filtered_by_rating[movie] = {"rating": details["rating"], "year": details["year"]}

    if filtered_by_rating:
        print(color_text(f"\nFiltered movies", GREEN))
        for movie, details in filtered_by_rating.items():
            print(f"{movie} ({details["year"]}): {details["rating"]}")
    else:
        print(color_text(f"No movies were filtered", RED))