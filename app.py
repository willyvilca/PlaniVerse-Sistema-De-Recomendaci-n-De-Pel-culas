import streamlit as st
import pandas as pd
import joblib
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Configurar la aplicación
st.set_page_config(page_title="PlaniVerse: Recomendador de Películas", page_icon="🎥", layout="wide")
st.markdown(
    """
    <style>
        /* Estilo general */
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #1e1e2f;
            color: white;
        }

        /* Banner principal */
        .banner {
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://source.unsplash.com/1600x400/?cinema,movie');
            background-size: cover;
            padding: 50px;
            text-align: center;
            color: #00bcd4;
            font-size: 2.5rem;
            border-bottom: 3px solid #00bcd4;
        }

        /* Separadores */
        .separator {
            margin: 30px 0;
            border-top: 2px solid #00bcd4;
        }

        /* Botones */
        .stButton button {
            background-color: #00bcd4;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 20px;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: #008c9e;
        }

        /* Carrusel de posters */
        .carousel {
            display: flex;
            gap: 20px;
            overflow-x: auto;
            scroll-behavior: smooth;
        }
        .carousel img {
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s;
        }
        .carousel img:hover {
            transform: scale(1.05);
        }

        /* Spinner personalizado */
        .spinner {
            border: 6px solid #1e1e2f;
            border-top: 6px solid #00bcd4;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Banner principal
st.markdown('<div class="banner">Bienvenido a PlaniVerse: Encuentra tu Próxima Película Favorita</div>', unsafe_allow_html=True)

# Cargar modelos y base de datos de películas
df = joblib.load('models/movie_db.df')
tfidf_matrix = joblib.load('models/tfidf_mat.tf')
tfidf = joblib.load('models/vectorizer.tf')
cos_mat = joblib.load('models/cos_mat.mt')

# Funciones
def obtener_recomendaciones_por_palabras_clave(keywords):
    keywords = keywords.split()
    keywords = " ".join(keywords)
    vector_keywords = tfidf.transform([keywords])
    resultado = cosine_similarity(vector_keywords, tfidf_matrix)
    peliculas_similares = sorted(list(enumerate(resultado[0])), reverse=True, key=lambda x: x[1])
    recomendaciones = [df.iloc[i[0]].title for i in peliculas_similares[1:6]]
    return recomendaciones

def obtener_recomendaciones_por_titulo(movie):
    index = df[df['title'] == movie].index[0]
    peliculas_similares = sorted(list(enumerate(cos_mat[index])), reverse=True, key=lambda x: x[1])
    recomendaciones = [df.iloc[i[0]].title for i in peliculas_similares[1:6]]
    return recomendaciones

def obtener_carteles(peliculas):
    ids = [df[df.title == i]['id'].values[0] for i in peliculas]
    carteles = []
    sinopsis = []
    for i in ids:
        url = f"https://api.themoviedb.org/3/movie/{i}?api_key=74c0e4cd54bbfc2cf0e587e232dbefc9"
        data = requests.get(url).json()
        poster_path = data.get('poster_path', None)
        overview = data.get('overview', "Sin información disponible.")
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else None
        carteles.append(full_path)
        sinopsis.append(overview)
    return carteles, sinopsis

# Separador visual
st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

# Lógica del sistema
df_titles = df.title.sort_values()
tipo_busqueda = st.sidebar.radio("Opciones de búsqueda", ('Películas por Título', 'Palabras Clave'))

if tipo_busqueda == 'Películas por Título':
    pelicula_nombre = st.selectbox('Selecciona una Película 🎬', df_titles)
    if st.button('Recomendar 🚀'):
        with st.spinner('Buscando recomendaciones...'):
            movies = obtener_recomendaciones_por_titulo(pelicula_nombre)
            posters, sinopsis = obtener_carteles(movies)
else:
    keyword = st.text_input('Introduce Palabras Clave 🌟', 'Ciencia Ficción')
    if st.button('Recomendar 🚀'):
        with st.spinner('Buscando recomendaciones...'):
            movies = obtener_recomendaciones_por_palabras_clave(keyword)
            posters, sinopsis = obtener_carteles(movies)

# Mostrar resultados
def mostrar_resultados(posters, movies, sinopsis):
    if posters:
        st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
        st.subheader("Recomendaciones 🎥")
        st.markdown('<div class="carousel">', unsafe_allow_html=True)
        for poster, movie, overview in zip(posters, movies, sinopsis):
            st.markdown(f'<div><img src="{poster}" width="150"/><p><strong>{movie}</strong></p><p>{overview[:100]}...</p></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if 'posters' in locals():
    mostrar_resultados(posters, movies, sinopsis)
