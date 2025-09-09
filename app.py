import pandas as pd
import streamlit as st

url = 'https://github.com/jsespecialista99-ops/IA/raw/refs/heads/main/datos_generales_ficticios.csv'
df = pd.read_csv(url, sep=';', encoding='utf-8')

st.title('Datos Generales Ficticios')
st.dataframe(df)
#Elegir Columnas
seleccion_columnas = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
DF = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')


df_serie_tiempo = df.copy()
df_serie_tiempo['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

# Cálculo Municipio con más delitos
max_municipio =df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]

# CONTRUIR LA PÁGINA
st.set_page_config(page_title='Dashboard de Delitos - Fiscalia', layout='wide')

st.header('Dashboard de Delitos - Fiscalía', anchor=None)
st.dataframe(DF)
st.markdown(f"Municipio con más delitos: {max_municipio}", unsafe_allow_html=True)
st.markdown(f"Cantidad de Delitos: {max_cantidad_municipio}", unsafe_allow_html=True)

st.subheader('Tipo de delito')
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)
