from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

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


if __name__ == '__main__':
    app.run(debug=True)