from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

app = Flask(__name__)

def load_data():
    return pd.read_csv('Western Wear.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movies_data = load_data()

    # Fetch user input
    movie_name = request.form['movie_name']

    # Selecting relevant features for recommendation
    selected_features = ['name', 'image']

    # Replace null values
    for feature in selected_features:
        movies_data[feature] = movies_data[feature].fillna('')

    # Combine selected features
    combined_features = movies_data['name'] + ' ' + movies_data['image']

    # Convert text to feature vectors
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(combined_features)

    # Calculate similarity scores
    similarity = cosine_similarity(feature_vectors)

    # Find close match for input movie
    find_close_match = difflib.get_close_matches(movie_name, movies_data['name'])
    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.name == close_match].index[0] # type: ignore

        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

        # Get top 10 recommendations
        recommended_movies = []
        for i, movie in enumerate(sorted_similar_movies[:10], 1):
            index = movie[0]
            title_from_index = movies_data.iloc[index]['name']
            Image_Url = movies_data.iloc[index]['image']
            recommended_movies.append((title_from_index, Image_Url))
        
        return render_template('recommendations.html', movie_name=movie_name, recommended_movies=recommended_movies)
    else:
        return render_template('not_found.html')

if __name__ == "__main__":
    app.run(debug=True)