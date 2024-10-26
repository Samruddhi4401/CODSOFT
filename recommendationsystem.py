movies = [
    {"title": "The Matrix", "genre": "Action"},
    {"title": "Toy Story", "genre": "Animation"},
    {"title": "The Godfather", "genre": "Crime"},
    {"title": "Inception", "genre": "Action"},
    {"title": "Finding Nemo", "genre": "Animation"},
    {"title": "The Shawshank Redemption", "genre": "Drama"},
    {"title": "The Dark Knight", "genre": "Action"},
    {"title": "Coco", "genre": "Animation"},
    {"title": "Pulp Fiction", "genre": "Crime"}
]

# Get user's favorite genre
user_genre = input("What is your favorite genre (e.g., Action, Animation, Crime, Drama)? ")

# Simple recommendation based on genre matching
def recommend_movies(genre):
    recommendations = [movie["title"] for movie in movies if movie["genre"].lower() == genre.lower()]
    return recommendations

# Generate recommendations
recommended_movies = recommend_movies(user_genre)

# Show the recommendations
if recommended_movies:
    print(f"Because you like {user_genre} movies, you might enjoy:")
    for movie in recommended_movies:
        print(f"- {movie}")
else:
    print("Sorry, we don't have recommendations for that genre right now.")
