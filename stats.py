from utils import color_text
from movie_storage import get_movies

# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"


def stats():
    """
    Loads the information from the JSON file.
    Calculates the average & median rating
    and lists the best & worst movie(s) based on their rating.
    """
    movies = get_movies()

    ratings = []
    for movie_name, details in movies.items():
        ratings.append(details["rating"])

    count = len(ratings)
    average_rating = sum(ratings) / count
    print(f"Average rating: {average_rating:.2f}")

    if count % 2 == 1:
        median_rating = ratings[count // 2]
    else:
        mid1 = ratings[count // 2 - 1]
        mid2 = ratings[count // 2]
        median_rating = (mid1 + mid2) / 2
    print(f"Median rating: {median_rating:.2f}")

    max_rating = max(ratings)
    best_movies = []
    for movie, details in movies.items():
        rating = details["rating"]
        if rating == max_rating:
            best_movies.append(movie)
    print(f"Best movie(s) with rating: {max_rating}:")
    for movie in best_movies:
        print(color_text(f"- {movie}", GREEN))

    min_rating = min(ratings)
    worst_movies = []
    for movie, details in movies.items():
        rating = details["rating"]
        if rating == min_rating:
            worst_movies.append(movie)
    print(f"Worst movie(s) with rating: {min_rating}:")
    for movie in worst_movies:
        print(color_text(f"- {movie}", GREEN))
