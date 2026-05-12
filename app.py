from flask import Flask, request, jsonify
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

movies = pickle.load(open('movies.pkl', 'rb'))
movies = movies.head(1000)

cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


@app.route('/')
def home():
    return "Movie Recommendation System Running"


@app.route('/recommend', methods=['POST'])
def recommend_movies():

    movie = request.json['movie']

    recommendations = recommend(movie)

    return jsonify({
        'recommendations': recommendations
    })


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)