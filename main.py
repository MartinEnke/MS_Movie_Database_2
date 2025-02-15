from utils import color_text
from menu import display_menu, user_choice

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


def main():
    print(color_text("\n********** MOVIE DATABASE **********", BLUE))
    while True:
        display_menu()
        user_choice()
        print("")


if __name__ == "__main__":
    main()
