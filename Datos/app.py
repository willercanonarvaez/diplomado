import streamlit as st

from cargar_datos import show_data_tab
from transformacion import show_transform_tab
from visualizaciones import show_visualization_tab
from mapa import show_map_tab
from evolucion import show_tab as show_evolucion_tab
from comparativo import show_tab as show_comparativo_tab
from cumplimiento_educativo import show_tab as show_riesgo_tab

# Agregar nueva pestaña
tabs = st.tabs([
    "📥 Carga de Datos", 
    "🔧 Transformación y Métricas", 
    "📊 Visualizaciones", 
    "🗺️ Mapa", 
    "📊 Comparativo", 
    "📉 Desempeño y Riesgo Educativo"
])

with tabs[0]:
    show_data_tab()
with tabs[1]:
    show_transform_tab()
with tabs[2]:
    show_visualization_tab()
with tabs[3]:
    show_map_tab()
with tabs[4]:
    show_comparativo_tab()  # así deberías llamar al módulo comparativo
with tabs[5]:
    show_riesgo_tab()

