import streamlit as st
import pandas as pd
import plotly.express as px
import os

def show_tab():
    st.markdown("## 📊 Comparativo Nacional de Indicadores")

    try:
        # Cargar bases
        info_2020 = pd.read_excel("Datos/Info_2020_2035.xlsx")
        info_2005 = pd.read_excel("Datos/Info_2005_2019.xlsx")

        # Mostrar resumen
        total_2020 = len(info_2020)
        total_2005 = len(info_2005)
        años_2020 = info_2020['AÑO'].nunique()
        años_2005 = info_2005['AÑO'].nunique()
        deptos_2020 = info_2020['DPNOM'].nunique()
        deptos_2005 = info_2005['DPNOM'].nunique()

        st.success("✅ **Bases cargadas correctamente:**")
        st.markdown(f"""
        - 📄 **Info_2020_2035.xlsx**: {total_2020:,} registros, {años_2020} años, {deptos_2020} departamentos  
        - 📄 **Info_2005_2019.xlsx**: {total_2005:,} registros, {años_2005} años, {deptos_2005} departamentos
        """)

        # Unificar
        df_dane = pd.concat([info_2005, info_2020], ignore_index=True)
        df_total = df_dane[df_dane["ÁREA GEOGRÁFICA"].str.lower().str.contains("total")]
        df_grouped = df_total.groupby(["DPNOM", "AÑO"], as_index=False)["Población"].sum()
        df_grouped.rename(columns={"DPNOM": "Departamento"}, inplace=True)

        # Datos educativos
        df_fact = st.session_state['df_fact']
        dim_geo = st.session_state['dim_geo']
        dim_tiempo = st.session_state['dim_tiempo']
        df_edu = df_fact.merge(dim_geo, on="id_geo").merge(dim_tiempo, on="id_tiempo")

        df_edu_grouped = df_edu.groupby(["departamento", "a_o"], as_index=False)["tasa_matriculaci_n_5_16"].mean()
        df_edu_grouped.rename(columns={"departamento": "Departamento", "a_o": "AÑO"}, inplace=True)

        # Merge
        df_comparado = df_edu_grouped.merge(df_grouped, on=["Departamento", "AÑO"], how="inner")

        # Treemap
        st.subheader("🌲 Treemap: Matrícula vs Población Proyectada")
        fig = px.treemap(
            df_comparado,
            path=['Departamento'],
            values='Población',
            color='tasa_matriculaci_n_5_16',
            color_continuous_scale='Viridis',
            hover_data={'AÑO': True, 'tasa_matriculaci_n_5_16': ':.2f'}
        )
        st.plotly_chart(fig, use_container_width=True)

        # Tabla
        st.subheader("📋 Tabla comparativa")
        st.dataframe(df_comparado.sort_values(by="AÑO", ascending=False))

        # Burbujas estáticas (promedios)
        st.subheader("🫧 Top 10 Departamentos por Población Promedio (5-16 años)")

        df_avg = df_grouped.groupby("Departamento", as_index=False)["Población"].mean()
        df_avg = df_avg.sort_values(by="Población", ascending=False).head(10)

        # Controles interactivos
        deptos_seleccionados = st.multiselect(
            "Selecciona los departamentos a mostrar",
            options=df_avg["Departamento"].tolist(),
            default=df_avg["Departamento"].tolist()
        )

        df_filtrado = df_avg[df_avg["Departamento"].isin(deptos_seleccionados)]

        fig_burbujas = px.scatter(
            df_filtrado,
            x="Departamento",
            y="Población",
            size="Población",
            color="Departamento",
            size_max=80,
            title="🔵 Población Promedio por Departamento (5-16 años)",
            labels={"Población": "Población 5-16"},
            height=600
        )
        fig_burbujas.update_layout(xaxis_tickangle=-45)

        st.plotly_chart(fig_burbujas, use_container_width=True)

    except Exception as e:
        st.error(f"❌ No se pudo cargar la base del DANE (`Info_2020_2035.xlsx`)\n\nError: {e}")


