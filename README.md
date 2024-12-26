📁 Dataset:
El conjunto de datos TMDB 5000 Movies, obtenido de Kaggle, sirve como base para el sistema de recomendación de películas. Incluye información como títulos de películas, géneros, sinopsis, reparto y equipo técnico. 🎥

⚙️ Tecnologías Utilizadas:
- Python 🐍
- Streamlit 🚀
- scikit-learn 📊
- Pandas 🐼
- NumPy 🔢

📝 Descripción:
El sistema de recomendación de películas utiliza el concepto de similitud del coseno y vectorización de palabras. Mediante el uso de incrustaciones de palabras (word embeddings), como Word2Vec o GloVe, transforma las sinopsis de las películas en vectores densos y calcula su similitud utilizando la similitud del coseno. Este enfoque ayuda a identificar películas similares basándose en sus descripciones textuales. 📚

📊 Características:
- Búsqueda de películas: Los usuarios pueden buscar películas por título o palabras clave.
- Recomendaciones de películas: Los usuarios reciben recomendaciones personalizadas de películas basadas en su entrada.
- Detalles de películas: Los usuarios pueden explorar información detallada sobre películas, incluyendo reparto, equipo técnico, géneros y sinopsis.

💻 Uso:
1. Instala las dependencias requeridas listadas en el archivo `requirements.txt`.
2. Ejecuta la aplicación web de Streamlit con el comando: `streamlit run app.py`.
3. Accede a la aplicación a través de la URL proporcionada, generalmente `http://localhost:8501`.

🌟 ¡Siéntete libre de explorar diferentes películas, descubrir recomendaciones y disfrutar de tu viaje cinematográfico! 🎉

📚 Referencias:
- TMDB 5000 Movies Dataset: [https://www.kaggle.com/tmdb/tmdb-movie-metadata](https://www.kaggle.com/tmdb/tmdb-movie-metadata)

📜 Licencia:
Este proyecto está licenciado bajo la Licencia MIT. Por favor, consulta el archivo `LICENSE` para más detalles.

🤝 Contribuciones:
¡Las contribuciones a este proyecto son bienvenidas! Siéntete libre de abrir issues o enviar pull requests.