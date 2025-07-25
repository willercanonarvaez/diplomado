import streamlit as st
import pandas as pd
import plotly.express as px

UST_BLUE = "#002855"
UST_YELLOW = "#FFD100"

def show_tab():
    st.title("📈 Evolución de Indicadores Educativos")

    if 'df_fact' not in st.session_state:
        st.warning("⚠️ Primero debes construir la tabla de hechos en la pestaña 'Transformación'.")
        return

    df_fact = st.session_state['df_fact']
    dim_geo = st.session_state['dim_geo']
    dim_tiempo = st.session_state['dim_tiempo']

    # Merge completo
    df = df_fact.merge(dim_geo, on='id_geo').merge(dim_tiempo, on='id_tiempo')
    df['departamento'] = df['departamento'].str.title()
    df['municipio'] = df['municipio'].str.title()

    st.subheader("🏆 Top 10 Municipios por Tasa de Matrícula")

    # Selector de departamento
    deptos = sorted(df['departamento'].unique())
    selected_depto = st.selectbox("Selecciona un departamento", deptos)

    # Selector de año
    años = sorted(df['a_o'].unique())
    selected_year = st.selectbox("Selecciona un año", años, index=len(años)-1)

    # Filtrar por departamento y año
    df_filtered = df[(df['departamento'] == selected_depto) & (df['a_o'] == selected_year)]

    if df_filtered.empty:
        st.warning("No hay datos disponibles para ese año y departamento.")
        return

    # Top 10 municipios
    top10 = df_filtered.groupby('municipio')['tasa_matriculaci_n_5_16'].mean().nlargest(10).reset_index()

    # Gráfico
    fig = px.bar(
        top10,
        x='tasa_matriculaci_n_5_16',
        y='municipio',
        color='municipio',
        orientation='h',
        title=f"Top 10 Municipios con Mayor Tasa de Matrícula en {selected_depto} - {selected_year}",
        labels={'tasa_matriculaci_n_5_16': 'Tasa de Matrícula (%)', 'municipio': 'Municipio'},
        height=600
    )

    fig.update_layout(
        xaxis_title='Tasa de Matrícula (%)',
        yaxis=dict(autorange='reversed'),
        showlegend=False,
        plot_bgcolor="#F5F5F5"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.subheader("🌡️ Mapa de Calor: Intensidad de Matrícula por Municipio y Año")

    selected_depto_heat = st.selectbox("Selecciona un departamento (heatmap)", deptos, index=deptos.index(selected_depto))

    df_heat = df[df['departamento'] == selected_depto_heat]
    df_heat = df_heat.groupby(['municipio', 'a_o'])['tasa_matriculaci_n_5_16'].mean().reset_index()

    if df_heat.empty:
        st.warning("No hay datos para este departamento.")
    else:
        # 🔹 Calcular top 10 municipios por promedio general
        top_municipios = (
            df_heat.groupby('municipio')['tasa_matriculaci_n_5_16']
            .mean()
            .nlargest(10)
            .index
        )

        df_top = df_heat[df_heat['municipio'].isin(top_municipios)]

        # 🔧 Convertir año a entero para que no aparezca como 2023.0
        df_top['a_o'] = df_top['a_o'].astype(int)

        # 🔁 Pivot para heatmap
        pivot_heat = df_top.pivot(index="municipio", columns="a_o", values="tasa_matriculaci_n_5_16")
        pivot_heat = pivot_heat.fillna(0)

        # 📊 Crear heatmap
        fig3 = px.imshow(
            pivot_heat,
            labels=dict(color="Tasa de Matrícula (%)"),
            color_continuous_scale="YlGnBu",
            aspect="auto",
            title=f"Top 10 Municipios por Tasa de Matrícula - {selected_depto_heat}"
        )

        fig3.update_layout(
            xaxis_title="Año",
            yaxis_title="Municipio",
            height=600
        )

        st.plotly_chart(fig3, use_container_width=True)
