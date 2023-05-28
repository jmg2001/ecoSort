import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title="EcoSort",
    page_icon="♻️",
    initial_sidebar_state="collapsed",
)

st.title(":green[EcoSort] ♻️",
         )

st.subheader("¡Bienvenido a nuestra plataforma de clasificación de residuos con inteligencia artificial!")

st.markdown(
    """
    Esto es EcoSort, tu asistente para clasificar tu basura de manera adecuada. En nuestro sitio web, hemos creado una 
    solución innovadora que utiliza algoritmos de inteligencia artificial para ayudarte a clasificar diferentes tipos 
    de residuos de manera eficiente y precisa. Con solo unos pocos clics, podrás identificar y categorizar residuos comunes, 
    contribuyendo así a un manejo adecuado y sostenible de los desechos.

    Nuestra plataforma combina la potencia del aprendizaje automático y la visión por computadora para analizar imágenes de 
    residuos. Simplemente carga una foto del residuo que deseas clasificar, y nuestra inteligencia artificial se encargará de 
    procesarla rápidamente, proporcionándote una clasificación precisa en cuestión de segundos.
    
    ### ¿Cómo funciona?
    
    Nuestra plataforma utiliza tecnología de inteligencia artificial para realizar la clasificación precisa de diferentes 
    tipos de residuos. El funcionamiento se basa en algoritmos de aprendizaje automático que han sido entrenados con una 
    amplia variedad de imágenes de residuos.

    Cuando cargas una imagen de residuo en nuestra plataforma, nuestro sistema de inteligencia artificial analiza automáticamente 
    las características visuales del objeto y las compara con un extenso conjunto de datos de entrenamiento. Esto nos permite 
    reconocer patrones y características distintivas que nos ayudan a determinar el tipo de residuo con una alta precisión.

"""
)


want_to_contribute = st.button("RECICLA AHORA")
if want_to_contribute:
    switch_page("Tira tu basura")