import sys
import random
import matplotlib.pyplot as plt
from movie_storage import get_movies, save_movies, add_movie, delete_movie, update_movie
from utils import color_text, get_movie_name, get_movie_rating, get_movie_year

"""
This program contains a json file which holds a dictionary
of a dictionary about movies, their year of appearance and their ratings.
It serves as a "Movie Database," offering features such as
listing, adding, deleting, updating, viewing statistics,
random selection, searching, sorting by ,
and filtering by rating or year.
It also provides the option to create a histogram based on the movie ratings.
To enhance the visual experience, various colors have been applied.
"""


# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"


def display_menu():
    """
    Contains the menu which is displayed to the user.
    """
    menu_text = """ 
Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Movies sorted by year
10. Filter movies
11. Create Rating Histogram
"""
    print(color_text(menu_text, BLUE))


def user_choice():
    """
    Effective choice menu.
    Will execute related options displayed in the menu.
    """
    movies = get_movies()
    choice = input(color_text("Enter choice (0-11): ", BLUE))
    if choice == "0":
        print("Bye!")
        sys.exit()
    elif choice == "1":
        print(color_text(f"{len(movies)} movies in total", GREEN))
        list_movies()
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "2":
        add_movie(get_movie_name, get_movie_rating, get_movie_year)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "3":
        delete_movie(get_movie_name)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "4":
        update_movie(get_movie_name, get_movie_rating)
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "5":
        stats()
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "6":
        random_movie()
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "7":
        search_movie()
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "8":
        movies_sorted_by_rating()
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "9":
        movies_sorted_by_year()
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "10":
       filtering_movies()
       print("")
       input(color_text("Press Enter to continue", YELLOW))
    elif choice == "11":
       rating_histogram()
       print("")
       input(color_text("Press Enter to continue", YELLOW))
    else:
        print(color_text("Invalid choice! Please enter a number between 0 and 11", RED))
        input(color_text("Press Enter to continue", YELLOW))


def list_movies():
    """
    Lists all movies of the movie database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    for movie_name, details in movies.items():
        print(f"{movie_name} ({details["year"]}): {details["rating"]}")


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


def filtering_movies():
    """
    Loads the information from the JSON file.
    Filters the movies based on minimum rating, as well as start & end year requested from the user.
    """
    movies = get_movies()
    while True:
        min_rating = input(color_text(f"Enter minimum rating (leave blank for no minimum rating): ", BLUE))
        if min_rating == "":  # Allowing blank input
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


def rating_histogram():
    """
    Loads the information from the JSON file.
    Creates a histogram based on the movie ratings.
    """
    movies = get_movies()
    ratings = []
    for movie, details in movies.items():
        ratings.append(details["rating"])  # extract ratings from dictionary

    # Create histogram
    plt.hist(ratings, bins=range(0, 11), edgecolor="yellow")  # Range 0-10 for ratings

    # labels and title
    plt.title('Movie Ratings Histogram')
    plt.ylabel('Frequency')
    plt.xlabel('Ratings')

    file_name = input(color_text("Enter filename to save histogram: ", BLUE))

    # Save plot to the file
    plt.savefig(file_name)
    print(color_text(f"Histogram successfully saved to '{file_name}'", GREEN))

    plt.show()


def main():
    print(color_text("\n********** MOVIE DATABASE **********", BLUE))
    while True:
        display_menu()
        user_choice()
        print("")


if __name__ == "__main__":
    main()
