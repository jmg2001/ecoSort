import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import folium
import statistics
from folium.plugins import MarkerCluster

st.set_page_config(
    page_title="Rutas",
    page_icon="🚛",
    initial_sidebar_state="collapsed",
)

@st.cache_data
def get_data(path):
    data = pd.read_csv(path)
    return data

data = get_data("puntosRecoleccion.csv")

nombres = data.iloc[:,5]
print(nombres[0])
locacion = data.iloc[:,10]
horario_fin = data.iloc[:,9]
horario_inicio = data.iloc[:,8]
dias = data.iloc[:,7]
locacionL = list()
latitudes = list()
longitudes = list()
for dato in locacion:
    latitudes.append(float(dato.split(",")[0]))
    longitudes.append(float(dato.split(",")[1]))
    locacionL.append([float(dato.split(",")[0]),float(dato.split(",")[1])])

m = folium.Map(location=[statistics.mean(latitudes),statistics.mean(longitudes)], zoom_start=10)
marker_cluster = MarkerCluster().add_to(m)

#@st.cache_resource
def create_marks():
    for i in range(0,len(locacion)):
        texto = f"""Locacion: {nombres[i]}
                    Horario Inicio: {horario_inicio[i]}
                    Horario Fin: {horario_fin[i]}
                    Dias: {dias[i]}"""
        folium.Marker(
            locacionL[i],
            popup=texto,
            tooltip=nombres[i],
        ).add_to(marker_cluster)

create_marks()

st.title("Puntos de recoleción 🚛")

st.markdown("""
        Aquí podrás identifar el punto de recollecion de residuos más cercano a tu domicilio
            """)

st_data = st_folium(m,width=725)

st.markdown("""
        Aquí podrás identifar el punto de recollecion de residuos más cercano a tu domicilio
            """)

st.stop()