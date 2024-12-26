import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Acerca de PlaniVerse", page_icon="ℹ️", layout="wide")

# CSS para personalizar la página
st.markdown("""
<style>
/* Fondo general */
.stApp {
    background-color: #f5f5f5;
}

/* Banner */
.banner {
    background: linear-gradient(90deg, #00bcd4, #1e1e2f);
    color: white;
    padding: 20px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    border-radius: 10px;
    margin-bottom: 20px;
}

/* Encabezados estilizados */
h1, h2, h3 {
    color: #00bcd4;
    font-family: 'Arial', sans-serif;
}

/* Contenedor para funcionalidades */
.funcionalidades {
    display: flex;
    justify-content: space-around;
    margin: 20px 0;
}

.funcionalidad {
    text-align: center;
    width: 30%;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
}

.funcionalidad img {
    width: 50px;
    height: 50px;
    margin-bottom: 10px;
}

hr {
    border: 1px solid #ddd;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)

# Banner
st.markdown('<div class="banner">🌟 Bienvenido a PlaniVerse 🌟</div>', unsafe_allow_html=True)

# Encabezados y descripción general
st.header("¿Qué es PlaniVerse?")
st.markdown("""
PlaniVerse es un recomendador de películas diseñado para ayudarte a descubrir tus próximos favoritos. Usamos tecnología avanzada de **machine learning** y una vasta base de datos de películas para ofrecerte recomendaciones personalizadas.

Con PlaniVerse puedes:
- Explorar nuevas películas según tus gustos.
- Descubrir películas similares a tus favoritas.
- Buscar usando palabras clave relacionadas con géneros, actores o temas.
""")

# Línea divisora
st.markdown("<hr>", unsafe_allow_html=True)

# Lista de funcionalidades con íconos
st.subheader("📌 Funcionalidades Principales")
st.markdown("""
<div class="funcionalidades">
    <div class="funcionalidad">
        <img src="https://via.placeholder.com/50?text=T" alt="Título">
        <h3>Búsqueda por Título</h3>
        <p>Introduce el título de una película que te guste y recibe recomendaciones similares.</p>
    </div>
    <div class="funcionalidad">
        <img src="https://via.placeholder.com/50?text=K" alt="Palabras clave">
        <h3>Palabras Clave</h3>
        <p>Encuentra películas usando términos específicos como géneros o temas.</p>
    </div>
    <div class="funcionalidad">
        <img src="https://via.placeholder.com/50?text=P" alt="Poster">
        <h3>Visualización de Póster</h3>
        <p>Obtén una vista previa del póster de cada película recomendada.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Línea divisora
st.markdown("<hr>", unsafe_allow_html=True)

# Explicación adicional con más detalles
st.subheader("🎯 ¿Por qué elegir PlaniVerse?")
st.markdown("""
PlaniVerse no es solo un recomendador, es una herramienta para cinéfilos y curiosos que buscan descubrir joyas ocultas en el mundo del cine. Nuestro sistema ofrece:
- **Recomendaciones personalizadas**: Basadas en algoritmos avanzados de similitud.
- **Interfaz intuitiva**: Fácil de usar, para que te centres en lo importante: las películas.
- **Datos actualizados**: Usamos una base de datos confiable para garantizar la calidad de las sugerencias.

Desarrollado por un equipo apasionado, PlaniVerse busca transformar cómo exploras y disfrutas del cine. ¡Prueba ahora y encuentra tu próxima película favorita!
""")

# Línea divisora
st.markdown("<hr>", unsafe_allow_html=True)

# Equipo de desarrollo (con íconos)
st.subheader("👩‍💻 Nuestro Equipo")
st.markdown("""
<div style='display: flex; justify-content: center; gap: 50px;'>
    <div style='text-align: center;'>
        <img src='wilmer.jpg' style='border-radius: 50%;' />
        <p><strong>Wilmer ticona</strong></p>
        <a href='https://github.com/Wilmer/' target='_blank'>GitHub</a>
    </div>
    <div style='text-align: center;'>
        <img src='https://avatars.githubusercontent.com/u/93614402?v=4' style='border-radius: 50%;' />
        <p><strong>Angel Garcia</strong></p>
        <a href='https://github.com/AngelgarciaJ/' target='_blank'>GitHub</a>
    </div>
    <div style='text-align: center;'>
        <img src='https://avatars.githubusercontent.com/u/171106543?v=4' style='border-radius: 50%;' />
        <p><strong>Willy Vilca</strong></p>
        <a href='https://github.com/willyvilca/' target='_blank'>GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Línea divisora
st.markdown("<hr>", unsafe_allow_html=True)

# Mensaje final
st.markdown("""
<div style="text-align: center; font-size: 18px; font-weight: bold;">
🎥 ¡Explora, descubre y disfruta del cine con PlaniVerse! 🎥
</div>
""", unsafe_allow_html=True)
