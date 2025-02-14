import json
from fileinput import close

import matplotlib.pyplot as plt


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


def color_text(text, color_code):
    # Applies an ANSI color code to the given text.
    return f"\033[{color_code}m{text}\033[0m"


# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"


def display_menu():
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
    movies = get_movies()
    choice = input(color_text("Enter choice (0-11): ", BLUE))
    if choice == "0":
        print("Bye!")
    elif choice == "1":
        print(color_text(f"{len(movies)} movies in total", GREEN))
        list_movies()
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "2":
        add_movie()
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "3":
        delete_movie()
        print("")
        input(color_text("Press Enter to continue", YELLOW))
    elif choice == "4":
        update_movie()
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
    #elif choice == "10":
    #    filtering_year(movies)
    #    print("")
    #    input(color_text("Press Enter to continue", YELLOW))
    # elif choice == "11":
    #    rating_histogram(movies)
    #    print("")
    #   input(color_text("Press Enter to continue", YELLOW))
    else:
        print(color_text("Invalid choice! Please enter a number between 1 and 8", RED))
        input(color_text("Press Enter to continue", YELLOW))


def get_movies():
    """
    Returns a dictionary of dictionaries that contains the movies information.
    """
    with open("movies.json", "r") as file:
        movies = json.loads(file.read())
    return movies


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open("movies.json", "w") as file:
        json.dump(movies, file)


def get_movie_name():
    movie = input(color_text("Enter movie name: ", BLUE)).title()
    return movie


def get_movie_rating():
    while True:
        rating = input(color_text("Enter movie rating (0-10): ", BLUE)).replace(",", ".")
        if rating.replace(".", "").isdigit():
            rating = float(rating)
            if 0.0 <= rating <= 10.0:
                return rating
            else:
                print(color_text("Rating must be between 0 and 10", RED))
        else:
            print(color_text("Invalid input. Please enter numeric value", RED))


def get_movie_year():
    while True:
        year = input(color_text("Enter movie year: ", BLUE)).strip()
        if year.isdigit():
            year = int(year)
            if 1900 < year < 2025:
                return year
            else:
                print(color_text("Rating must be between 0 and 10", RED))
        else:
            print(color_text("Invalid input. Please enter numeric value", RED))


def list_movies():
    """
    Lists all movies of the movie database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    for movie_name, details in movies.items():
        print(f"{movie_name} ({details["year"]}): {details["rating"]}")


def add_movie():
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
    print(color_text(f"Movie '{movie}' successfully added", GREEN))


def delete_movie():
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


def update_movie():
    """
    Updates a movie from the movie database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    movie = get_movie_name()
    if movie in movies:
        rating = get_movie_rating()
        year = get_movie_year()
        movies[movie] = {"rating": rating, "year":year}
        print(color_text(f"Movie '{movie}' successfully updated", GREEN))
    else:
        print(color_text(f"Movie '{movie}' doesn't exist", RED))
        return

    save_movies(movies)



def stats():
    """"""
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


'''
def random_movie(movies):
    movie = random.choice(list(movies.keys()))
    rating = movies[movie]
    print(color_text(f"Your movie for tonight: '{movie}', Rating: {rating}", GREEN))


def search_movie(movies):
    movie = get_movie_name().casefold()
    found = False
    for movies, ratings in movies.items():
        if movie in movies.casefold():
            # str-length: 3 char minimum
            if len(movie) > 2:
                print(color_text(f"- {movies}: {ratings}", GREEN))
                found = True
    if not found:
        print(color_text("No entry under this name", RED))


def movies_sorted_by_rating(movies):
    # dict conversion into two lists for movies & their ratings
    movie_names = list(movies.keys())
    movie_ratings = list(movies.values())

    for i in range(len(movie_ratings)):
        for j in range(i + 1, len(movie_ratings)):
            # Compare ratings
            if movie_ratings[i] < movie_ratings[j]:
                # Swap ratings - if lower rating first
                movie_ratings[i], movie_ratings[j] = movie_ratings[j], movie_ratings[i]
                # Swap corresponding movie names
                movie_names[i], movie_names[j] = movie_names[j], movie_names[i]

    for i in range(len(movie_names)):
        print(color_text(f"- {movie_names[i]}: {movie_ratings[i]}", GREEN))

'''



def rating_histogram(movies):
    ratings = list(movies.values())  # extract ratings from dictionary

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
