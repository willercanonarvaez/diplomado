import streamlit as st
import pandas as pd
import plotly.express as px

def show_tab():
    st.markdown("## 📉 Desempeño y Riesgo Educativo")
    st.caption("Analiza los indicadores clave como **deserción**, **aprobación** y **repitencia** a nivel departamental.")

    if 'df_clean' not in st.session_state:
        st.warning("⚠️ Primero debes cargar y transformar los datos en la pestaña de Transformación.")
        return

    df = st.session_state['df_clean']

    # Selección de año
    años_disponibles = sorted(df['a_o'].unique())
    año_seleccionado = st.selectbox("📅 Selecciona un año:", años_disponibles, index=len(años_disponibles)-1)
    df_filtrado = df[df['a_o'] == año_seleccionado]

    # Normalizar nombre largo de San Andrés
    df_filtrado['departamento'] = df_filtrado['departamento'].replace({
        "Archipiélago De San Andrés Providencia Y Santa Catalina": "San Andrés"
    })

    st.subheader("📦 Distribución de la Deserción por Departamento")

    # Departamento selector interactivo (máx. 5 visibles en gráfico)
    departamentos_unicos = sorted(df_filtrado['departamento'].unique())
    departamentos_seleccionados = st.multiselect(
        "🏷️ Selecciona hasta 5 departamentos:",
        departamentos_unicos,
        default=departamentos_unicos[:5],
        max_selections=5,
        key="select_departamentos_boxplot"
    )

    df_box = df_filtrado[df_filtrado['departamento'].isin(departamentos_seleccionados)]

    fig_box = px.box(
        df_box,
        x="departamento",
        y="deserci_n",
        points="all",
        color="departamento",
        labels={"deserci_n": "Deserción (%)"},
        title=f"Distribución de la Deserción - Año {año_seleccionado}"
    )
    fig_box.update_layout(showlegend=False, height=600, margin=dict(l=30, r=30, t=60, b=30))
    st.plotly_chart(fig_box, use_container_width=True)

    st.markdown("---")
    st.subheader("📊 Comparativo de Indicadores Clave por Departamento")

    st.markdown("---")
    st.subheader("🧭 Comparativo 3D: Aprobación, Repitencia y Reprobación")

    # Filtrado para valores válidos
    df_3d = df_filtrado[['departamento', 'aprobaci_n', 'repitencia', 'reprobaci_n']].dropna()

    fig_3d = px.scatter_3d(
        df_3d,
        x='aprobaci_n',
        y='repitencia',
        z='reprobaci_n',
        color='departamento',
        hover_name='departamento',
        title=f"📌 Indicadores Clave por Departamento - Año {año_seleccionado}",
        labels={
            'aprobaci_n': 'Aprobación (%)',
            'repitencia': 'Repitencia (%)',
            'reprobaci_n': 'Reprobación (%)'
        },
        height=700
    )
    fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=40))

    st.plotly_chart(fig_3d, use_container_width=True)
