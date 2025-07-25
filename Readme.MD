# Proyecto Diplomado Gestión de Datos

## 🧩 Tecnologías utilizadas

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-%3E%3D2.3.0-%2332CD32)
![NumPy](https://img.shields.io/badge/NumPy-%3E%3D2.3.0-%23008080)
![Seaborn](https://img.shields.io/badge/Seaborn-%3E%3D0.13.2-%23FF69B4)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%3E%3D3.10.3-%23FF8C00)
![Streamlit](https://img.shields.io/badge/Streamlit-%3E%3D1.46.1-%23FF4B4B)
![Plotly](https://img.shields.io/badge/Plotly-%3E%3D6.2.0-%236A5ACD)
![Folium](https://img.shields.io/badge/Folium-%3E%3D0.20.0-%23C71585)
![OpenPyXL](https://img.shields.io/badge/OpenPyXL-%3E%3D3.1.5-%2300BFFF)
![GeoPandas](https://img.shields.io/badge/GeoPandas-%3E%3D1.1.1-%239ACD32)
![streamlit-folium](https://img.shields.io/badge/Streamlit--Folium-%3E%3D0.25.0-%23F08080)


# 📊 Análisis Educativo y Modelo Dimensional - Trabajo Final

Este repositorio contiene una recopilación de trabajos realizados durante el curso, incluyendo ejercicios en clase con los docentes y entregas individuales desarrolladas. El objetivo principal fue aplicar conocimientos en modelado de datos, análisis exploratorio y visualización interactiva usando Python y Streamlit.

## 🧠 ¿Qué puedes encontrar aquí?

### 1. `Trabajo_final_modelo_dimensional/`
Carpeta dedicada al desarrollo de un **modelo dimensional tipo estrella** aplicado a datos educativos en Colombia.

🧱 **Construcción del modelo dimensional en estrella**  
El primer paso fue la integración y limpieza de múltiples fuentes de datos: la base de DIVIPOLA (con códigos y nombres oficiales de municipios), el conjunto de estadísticas del MEN (Ministerio de Educación Nacional) y dos bases de proyecciones poblacionales del DANE (2005–2019 y 2020–2035). Estas proyecciones se unificaron para construir una base única de población escolar entre 5 y 16 años, fundamental para calcular tasas e indicadores.

Se realizó una normalización semántica de nombres de municipios y departamentos eliminando tildes, caracteres especiales y diferencias de formato. Esta limpieza permitió hacer una unión efectiva entre el MEN y DIVIPOLA, alcanzando un nivel de coincidencia superior al 97%, garantizando consistencia geográfica.

🧭 **Definición de dimensiones y tabla de hechos**  
Con los datos consolidados, se construyeron tres componentes esenciales del modelo:

- **Dimensión Geográfica (`dim_geo`)**: contiene códigos y nombres únicos para departamentos y municipios, junto con coordenadas geográficas.
- **Dimensión de Tiempo (`dim_tiempo`)**: construida a partir de los años disponibles en los datos del MEN.
- **Tabla de Hechos (`fact`)**: integra población entre 5-16 años, matrícula, tasa de matrícula, cobertura, aprobación, deserción y repitencia.

🧮 **Consultas SQL para escolaridad y cobertura**  
Se implementó una base SQLite para realizar consultas SQL:
- Query 1: % de escolaridad por municipio.
- Query 2: Tasa promedio de matrícula.
- Query 3: Ranking de departamentos con mejor cobertura.

📊 **Visualizaciones interactivas**
- Barras horizontales (top 15 municipios con mayor escolaridad).
- Gráfico de burbujas ordenadas por matrícula.
- Barras verticales con degradado por cobertura departamental.

🧠 **Análisis interpretativo**  
Se incluyeron descripciones para interpretar cobertura, brechas educativas y desafíos territoriales, destacando departamentos que superan el 95% de cobertura.

---
# Trabajo streamli

Se desarrolló un trabajo adicional donde se implementó la misma base de datos del modelo dimensional en educación. En esta ocasión, el objetivo fue construir una aplicación en Streamlit estructurada en diferentes archivos .py. En primer lugar, se cargó la base de datos original; posteriormente, se realizó el proceso de limpieza, creación de dimensiones y construcción de la tabla de hechos. A partir de allí, se diseñaron diversos gráficos interactivos con un enfoque innovador. No solo se buscó interactividad, sino también coherencia en la selección de variables, de manera que cada visualización permitiera interpretar fenómenos educativos relevantes y generara resultados precisos y comprensibles.

### 2. `app.py` y módulos `.py` auxiliares
Aplicación construida con **Streamlit** para explorar de forma interactiva los datos transformados. Dividida en pestañas:

#### 📥 `Carga de Datos`
Carga inicial y validación de la base del MEN.

#### 🔧 `Transformación y Métricas`
Limpieza y construcción del modelo estrella, integración con DIVIPOLA y DANE.

#### 📊 `Visualizaciones`
Mapas y gráficos por municipio y departamento.

#### 🗺️ `Mapa`

Mapa interactivo por departamento con su cobertura neta.

#### 📈 `Comparativo Nacional`
Cruces con proyecciones poblacionales. Incluye gráficos tipo Treemap y burbujas.

#### 📉 `Cumplimiento y Riesgo Educativo`
Análisis de deserción, aprobación y repitencia por departamento. Visualizaciones dinámicas con selección y comparación.

---

## 🚀 Cómo correr la aplicación
```bash
poetry run streamlit run Datos/app.py
```

---

## ✍️ Autor
Trabajo realizado por Willer Cano Narvaez estudiante de la universdiad Santo Tomas de colombia como parte del curso de análisis y visualización de datos. Se integraron herramientas de ingeniería de datos, SQL, modelos dimensionales y Streamlit.
