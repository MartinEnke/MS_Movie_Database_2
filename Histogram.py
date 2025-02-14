import matplotlib.pyplot as plt

# Example dictionary
movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }

# Extract keys and values from the dictionary
labels = list(movies.keys())  # Labels for the x-axis
values = list(movies.values())  # Values for the y-axis

# Create the histogram
plt.bar(labels, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Histogram from Dictionary')

# Show the plot
plt.show()
