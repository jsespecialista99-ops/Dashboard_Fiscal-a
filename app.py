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




import pandas as pd
import streamlit as st

url2 = 'https://github.com/jsespecialista99-ops/IA/raw/refs/heads/main/datos_generales_ficticios.csv'
df2 = pd.read_csv(url, sep=';', encoding='utf-8')

st.dataframe(df)

# Crear lista de Columnas de Interes
seleccion_columnas = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
# Actualizo el DataFrame -df2- con las columnas de interes, ordenado por fecha y reseteo el indice
DF2 = df2[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)


# Convierto la columna FECHA_HECHOS a formato fecha
df2['FECHA_HECHOS'] = pd.to_datetime(df2['FECHA_HECHOS'], errors='coerce')
# Extraigo solo la fecha (sin hora)
df_serie_tiempo['FECHA_HECHOS'] = df2['FECHA_HECHOS'].dt.date

# Calculo Municipio con más delitos
max_municipio =df2['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
st.write(f'# Municipio Top Delitos: {max_municipio}')

max_cantidad_municipio = df2['MUNICIPIO_HECHOS'].value_counts().iloc[0]
st.write(f'# Eventos: {max_cantidad_municipio}') 

# CONTRUIR LA PÁGINA
st.set_page_config(page_title='Dashboard de Delitos - Fiscalia', layout='wide')
st.header('Dashboard de Delitos - Fiscalía')
#st.markdown(f"<center><h1>Dashboard de Delitos - Fiscalía</center>", unsafe_allow_html=True)

st.dataframe(DF2)

st.write(f'### Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} Eventos')
#st.write(f'### Cantidad de Eventos: {max_cantidad_municipio}')

#st.subheader('Tipo de delito')
