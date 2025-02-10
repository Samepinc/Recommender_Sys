import pickle
import numpy as np
import pandas as pd
import streamlit as st
import requests

try:
    def fetch_poster(movie_id):
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url)
        data = data.json()
        poster_path = data['poster_path']
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path

    def recommend(movie,joun,year):

        index = movies[movies['movie_name'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies=[]
        recommended_movie_posters = []
        count=0
        for i in distances[1:]:
            if count>=5:
                break
            else:
                if joun in movies.iloc[i[0]].tags and int(movies.iloc[i[0]].year) in year_l :
                    count+=1
                    recommended_movies.append(movies.iloc[i[0]].movie_name)
                    movie_id = movies.iloc[i[0]].movie_id
                    recommended_movie_posters.append(fetch_poster(movie_id))
        return recommended_movies,recommended_movie_posters
    movie_dict=pickle.load(open('movie_dict.pkl', 'rb'))
    movies=pd.DataFrame(movie_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    st.title("Movie Recommender System ")
    selected_movie_name = st.selectbox(
        "Select Movie Recommender System",
        (movies['movie_name'].values)
    )
    jounr = st.selectbox(
        "Select Movie Recommender System",
        ("Action","Crime","Romance","Thriller","Comedy")
    )
    selected_year= st.selectbox("Select Movie Recommender System",("1980",'2000','2020'))
    year = int(selected_year)
    year_l=[]
    for i in range(-10,10,1):
        year_l.append(year-i)
    if st.button("Recommend"):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name,jounr,year)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
except KeyError:
    st.text("Sorry, the selected Movie Recommender System is not available due to non availability of Poster")