import streamlit as st
import pickle
import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# --------------------------
# SAFE POSTER FETCH FUNCTION
# --------------------------
def fetch_poster(movie_id):
    api_key = "7501a50a287441878eda1bd8e30ca822"
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7501a50a287441878eda1bd8e30ca822&language=en-US".format(movie_id)

    # Retry session setup
    session = requests.Session()
    retries = Retry(
        total=3,                # Retry 3 times
        backoff_factor=0.5,     # Wait between retries
        status_forcelist=[429, 500, 502, 503, 504]
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))

    try:
        response = session.get(url, timeout=7)  
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except Exception as e:
        print("Error fetching poster:", e)
        return "https://via.placeholder.com/500x750?text=No+Image"

# --------------------------
# RECOMMEND FUNCTION
# --------------------------

def recommend(movie_name):
    movie_name = movie_name.lower().strip()  # safe matching

    # Case-insensitive search
    matched_movies = movies_list[movies_list['title'].str.lower() == movie_name]
    if matched_movies.empty:
        # Return placeholders if movie not found
        return ["Movie not found"]*5, ["https://via.placeholder.com/500x750?text=No+Image"]*5

    movie_index = matched_movies.index[0]

    # Get similarity scores and top 5 recommendations
    distances = similarity[movie_index]
    movie_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in movie_list1:
        movie_id = movies_list.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies_list.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters



# --------------------------
# LOAD DATA
# --------------------------
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = movies_list['title'].values



# --------------------------
# STREAMLIT UI
# --------------------------
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a movie:", movies)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i])
