import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub
from streamlit_extras.let_it_rain import rain
import configparser

config = configparser.ConfigParser()

def make_ini(list):
    config.add_section("counters")
    for item in list:
        config.set('counters',  item, 0)
        with open(r'pages/config.ini', 'w') as configfile:
                config.write(configfile)

def save_number_to_ini(name, number):
    config['counters'] = {f'{name}': str(number)}

    with open('config.ini', 'w') as config_file:
        config.write(config_file)

class_names = ['Cartón', 'Vidrio', 'Metal', 'Papel', 'Plastico', 'Basura']

make_ini(class_names)

st.set_page_config(
    page_title="Tira tu basura",
    page_icon="🗑️",
    initial_sidebar_state="collapsed",
)

@st.cache_resource
def create_model(path):
    model = keras.models.load_model(path,custom_objects={'KerasLayer':hub.KerasLayer})
    return model
count = 0
if count == 0:
    modelo = create_model("modelo_91.h5")
    count = 1


st.title("Tira tu basura aquí:",)

st.markdown(
    """
    Abre la camara y toma una foto a tu basura, nuestro algoritmo de clasificación
    de imagenes utilizando ``Tensorflow`` nos permite poder decidir que tipo de basura
    tienes.

    """
)

img_file_buffer = st.camera_input("Take a picture",label_visibility="hidden")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    img_res = cv2.resize(cv2_img, (224,224))
    img_res = img_res/255.0
    imagenFinal = tf.expand_dims(img_res, axis=0)

    prediccion = modelo.predict(imagenFinal)
    prediccion = tf.squeeze(prediccion)

    maxIndex = tf.argmax(prediccion).numpy()

    btn = st.download_button(
            label="Guardar",
            data=bytes_data,
            file_name="Basura.png",
            mime="image/png"
          )
    
    st.title(f"Tu residuo fue clasificado como: {class_names[maxIndex]}")

    config.read('config.ini')
    material = int(config.get('counters', f'{class_names[maxIndex]}')) + 1
    save_number_to_ini(class_names[maxIndex], material)
    st.title(f"Has ayudado a prevenir el desecho de {material} de {class_names[maxIndex]}")

    if maxIndex == 0:
        emoji = "📦"
    if maxIndex == 1:
        emoji = "🍾"
    if maxIndex == 2:
        emoji = "⚙️"
    if maxIndex == 3:
        emoji = "📄"
    if maxIndex == 4:
        emoji = "🔫"
    if maxIndex == 5:
        emoji = "🗑️"

    rain(
        emoji=emoji,
        font_size=54,
        falling_speed=1,
        animation_length=1,
    )
