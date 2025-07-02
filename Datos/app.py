import streamlit as st

from cargar_datos import show_data_tab
from transformacion import show_transform_tab
from visualizaciones import show_visualization_tab

# Crear pestañas en el cuerpo de la aplicación
tabs = st.tabs(["📥 Carga de Datos", "🔧 Transformación y Métricas", "📊 Visualizaciones", "🗺️ Mapa"])

# Mostrar contenido en cada pestaña
with tabs[0]:
    show_data_tab()

with tabs[1]:
    show_transform_tab()

with tabs[2]:
    show_visualization_tab()

import pydeck as pdk

if 'dim_geo' in st.session_state:
    geo_df = st.session_state['dim_geo'].copy()

    # 🔧 Asegúrate de tener lat/lon. Si no las tienes, este es un ejemplo simulado:
    geo_df['lat'] = geo_df['departamento'].map({
        'Bogotá, D.C.': 4.7110,
        'Antioquia': 6.2518,
        'Valle del Cauca': 3.4516,
        # Agrega más departamentos con coordenadas
    })
    geo_df['lon'] = geo_df['departamento'].map({
        'Bogotá, D.C.': -74.0721,
        'Antioquia': -75.5636,
        'Valle del Cauca': -76.5320,
        # Agrega más coordenadas
    })

    geo_df = geo_df.dropna(subset=['lat', 'lon'])

    layer = pdk.Layer(
        "ScatterplotLayer",
        geo_df,
        get_position='[lon, lat]',
        get_radius=40000,
        get_fill_color='[255, 140, 0, 140]',
        pickable=True
    )

    view_state = pdk.ViewState(
        latitude=4.5709,
        longitude=-74.2973,
        zoom=5
    )

    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=view_state,
        layers=[layer],
        tooltip={"text": "{departamento}\n{municipio}"}
    ))
else:
    st.warning("❌ No hay datos cargados para el mapa.")

