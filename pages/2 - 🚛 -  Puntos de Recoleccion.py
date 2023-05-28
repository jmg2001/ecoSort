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

@st.cache_resource
def get_data(path):
    data = pd.read_csv(path)
    return data
count = 0
if count == 0:
    data = get_data("pages\puntosRecoleccion.csv")
    count = 1

nombres = data.iloc[:,5]
locacion = data.iloc[:,10]
locacionL = list()
latitudes = list()
longitudes = list()
for dato in locacion:
    latitudes.append(float(dato.split(",")[0]))
    longitudes.append(float(dato.split(",")[1]))
    locacionL.append([float(dato.split(",")[0]),float(dato.split(",")[1])])

@st.cache_resource
def create_map():
    m = folium.Map(location=[statistics.mean(latitudes),statistics.mean(longitudes)], zoom_start=16)
    marker_cluster = MarkerCluster().add_to(m)
    return m, marker_cluster
count = 0
if count == 0:
    m, marker_cluster = create_map()
    count = 1

for i in range(0,len(locacion)):
    folium.Marker(
        locacionL[i],
        popup=nombres[i],
        tooltip=nombres[i],
    ).add_to(marker_cluster)

st.title("Puntos de recoleción 🚛")

st.markdown("""
        Aquí podrás identifar el punto de recollecion de residuos más cercano a tu domicilio
            """)

st_data = st_folium(m,width=725)