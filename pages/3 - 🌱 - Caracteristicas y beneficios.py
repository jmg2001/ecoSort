import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
import statistics
from folium.plugins import MarkerCluster

st.set_page_config(
    page_title="Caracteristicas y beneficios",
    page_icon="🌱",
    initial_sidebar_state="collapsed",
)
st.title("Características:")
st.markdown("""
- Precisión y confiabilidad: El proyecto utiliza algoritmos de inteligencia artificial y técnicas avanzadas de procesamiento de imágenes para lograr una clasificación precisa de los diferentes tipos de residuos. Esto garantiza resultados confiables y evita errores comunes en la clasificación manual.

- Eficiencia y velocidad: La clasificación de residuos mediante inteligencia artificial es un proceso rápido y eficiente. Los resultados se obtienen en cuestión de segundos, lo que permite ahorrar tiempo y recursos en comparación con los métodos de clasificación tradicionales.

- Amplia variedad de tipos de residuos: El sistema está diseñado para reconocer y clasificar una amplia gama de tipos de residuos, incluyendo papel, plástico, vidrio, metal, cartón, materia orgánica, electrónicos, entre otros. Esto asegura que puedas clasificar diferentes tipos de residuos con una sola plataforma.

- Facilidad de uso: El proyecto se desarrolla con una interfaz de usuario intuitiva y fácil de usar. Los usuarios pueden capturar imágenes de los residuos a través de dispositivos móviles o cargar imágenes desde sus computadoras, lo que simplifica el proceso de clasificación.
""")

st.title("Beneficios:")
st.markdown("""
- Promoción de la conciencia ambiental: Al facilitar la clasificación adecuada de los residuos, el proyecto contribuye a aumentar la conciencia ambiental y promover prácticas de reciclaje adecuadas. Esto ayuda a reducir la contaminación y el impacto negativo en el medio ambiente.

- Optimización de la gestión de residuos: La clasificación precisa de los residuos proporciona información valiosa para mejorar la gestión de residuos. Permite identificar patrones y tendencias en la generación de residuos, lo que puede ayudar a tomar decisiones informadas sobre estrategias de reciclaje, reutilización y reducción de residuos.

- Facilita el reciclaje y la reutilización: Al identificar correctamente los tipos de residuos, el proyecto facilita el proceso de reciclaje y reutilización. Los usuarios pueden tomar decisiones más informadas sobre cómo desechar los residuos, identificar los puntos de reciclaje adecuados y fomentar la separación adecuada de los materiales reciclables.

- Contribuye a un futuro sostenible: Al utilizar tecnologías avanzadas como la inteligencia artificial, el proyecto se alinea con los objetivos de sostenibilidad y protección del medio ambiente. Ayuda a construir un futuro más limpio y sostenible al fomentar prácticas responsables de manejo de residuos y promover la economía circular.
""")