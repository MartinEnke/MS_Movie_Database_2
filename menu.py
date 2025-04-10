import sys
from stats import stats
from movie_storage import list_movies, add_movie, delete_movie, update_movie
from utils import color_text, BLUE, RED, YELLOW, GREEN, get_movie_name, get_movies, get_movie_rating, get_movie_year
from process_movies import (random_movie, search_movie,
                            movies_sorted_by_rating, movies_sorted_by_year, movies_sorted_by_alphabet, filtering_movies)


def display_menu():
    """
    Contains the menu which is displayed to the user.
    """
    menu_text = """Menu:
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
10. Movies sorted alphabetically
11. Filter movies
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
       movies_sorted_by_alphabet()
       print("")
       input(color_text("Press Enter to continue", YELLOW))
    elif choice == "11":
       filtering_movies()
       print("")
       input(color_text("Press Enter to continue", YELLOW))
    else:
        print(color_text("Invalid choice! Please enter a number between 0 and 11", RED))
        input(color_text("Press Enter to continue", YELLOW))
