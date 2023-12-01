import streamlit as st
import pickle
import requests
import pandas as pd

def fetch_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8fe08ca3bb37030ce26bc59bfbecf201&language=en-US'.format(id))
    data = response.json()
    #st.write(data)
    #st.write(response)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recom(m):
    m_index = movies[movies['title'] == m].index[0]
    dist = similarity[m_index]
    l = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]
    recom_movies = []
    recom_posters = []
    for i in l:
        m_id = movies.iloc[i[0]].movie_id
        recom_movies.append(movies.iloc[i[0]].title)
        recom_posters.append(fetch_poster(m_id))
    return recom_movies, recom_posters

movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
#movies_list = pickle.load(open('movies.pkl', 'rb'))
#movies = movies_list['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommend System')

selected_movie = st.selectbox( 'What to recommend :', movies['title'].values)

if st.button('Show Recommendation'):
    names, posters = recom(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
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