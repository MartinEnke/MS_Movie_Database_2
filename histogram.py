from utils import color_text, BLUE, GREEN
import matplotlib.pyplot as plt
from movie_storage import get_movies




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