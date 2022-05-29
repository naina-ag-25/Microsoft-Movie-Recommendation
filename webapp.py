import streamlit as st
import pandas as pd
import pickle
import requests
from PIL import Image

st.set_page_config(page_title='Microsoft Recommender',
                        page_icon='mslogo.jpeg')

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{'
                 '}?api_key=a85c60b1cc3276bccfea19049f6edd53&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1] )[1:11]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
'Microsoft Intern Engage 2022 Project',
movies['title'].values
)



if st.button('Recommend'):
    st.text('------:   Recommended Movies   :------')
    names,posters = recommend(selected_movie_name)

    col1, col2,col3, col4,col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

    col1, col2,col3, col4,col5= st.columns(5)
    with col1:
        st.text(names[5])
        st.image(posters[5])
    with col2:
        st.text(names[6])
        st.image(posters[6])
    with col3:
        st.text(names[7])
        st.image(posters[7])
    with col4:
        st.text(names[8])
        st.image(posters[8])
    with col5:
        st.text(names[9])
        st.image(posters[9])

st.text('Made by Naina Agarwal')
