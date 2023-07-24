import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset (User ratings for movies)
data = {
    'User1': [5, 4, 2, 1, 5],
    'User2': [1, 2, 5, 4, 4],
    'User3': [3, 5, 4, 3, 2],
    'User4': [2, 3, 5, 5, 3],
    'User5': [4, 2, 3, 5, 1],
}

# Create a DataFrame from the data
df = pd.DataFrame(data, index=['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'])

def recommend_movies(user, num_recommendations=3):
    # Calculate similarity between the input user and all other users
    similarities = cosine_similarity(df.fillna(0), df.loc[user].fillna(0).values.reshape(1, -1))
    
    # Convert the similarity scores into a DataFrame
    sim_df = pd.DataFrame(similarities, columns=df.index, index=df.index)
    
    # Sort the movies based on similarity with the input user (excluding the input user itself)
    sorted_similarities = sim_df.drop(user).sort_values(by=user, ascending=False)
    
    # Get the top n similar users
    top_similar_users = sorted_similarities.index[:num_recommendations]
    
    # Get the recommendations based on the movies highly rated by the top similar users
    recommended_movies = df.loc[top_similar_users].mean().sort_values(ascending=False)
    
    return recommended_movies.index[:num_recommendations]

# Test the recommendation system for User1
user_to_recommend = 'User1'
recommendations = recommend_movies(user_to_recommend)

print(f"Recommended movies for {user_to_recommend}:")
for i, movie in enumerate(recommendations, 1):
    print(f"{i}. {movie}")
