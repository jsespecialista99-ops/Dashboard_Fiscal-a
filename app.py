import pandas as pd
import streamlit as st
import plotly.express as px


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

# Calculo de la etapa que más veces se presenta
# Ya que value_counts() genera un dataframe ordenado, traigo solo el primer indice .index[0] 
# etapa_mas_frecuente = df2['ETAPA'].value_counts().index[0]
etapa_mas_frecuente = df2['ETAPA'].value_counts().index[0].upper()
# ya que value_counts() genera un dataframe ordenado, traigo solo el primer valor .iloc[0] 
cant_etapa_mas_frecuente = df2['ETAPA'].value_counts().iloc[0]


# Construir página
st.set_page_config(page_title='Dashboard de Delitos - Fiscalía', layout='wide')
st.markdown(
    """
    <style>
    .block-container {
        padding: 1rem 2rem 2rem 2rem;
        max-width: 1600px;
    }    
    </style>
    """,
    unsafe_allow_html=True
)

st.image('Encabezado/Encabezado.png', use_container_width=True)

# gráfico de barras apiladas

st.subheader('Delitos por Departamento')
df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', title='Delitos por Departamento', barmode='stack')
st.plotly_chart(fig, key='bar_departamentos')
fig.update_layout(showlegend=False, height=400)


col1, col2, col3, col4 = st.columns(4)

with col1:

    # Tarjetas
    st.markdown(f"""<h3 style='color:#F2A88D;
                background-color:#FFF6F5;
                border: 2px solid #F2A88D; 
                border-radius: 10px; 
                padding: 10px; 
                text-align: center'> Municipio con más delitos: {max_municipio}</h3><br>""", 
                unsafe_allow_html=True
    )
with col2:  

    st.markdown(f"""<h3 style='color:#F2A88D;
                background-color:#FFF6F5;
                border: 2px solid #F2A88D; 
                border-radius: 10px; 
                padding: 10px; 
                text-align: center'> Delitos Reportados<br> {max_cantidad_municipio} </h3><br>""", 
                unsafe_allow_html=True
    )

with col3:
	## Tarjeta 3 - Etapa mas recurrente
	st.markdown(f"""<h3 style=
				'color:#A6886D;
				background-color:#F7EBD6;
				border: 2px solid #A6886D;
				border-radius: 10px; padding: 10px;
				text-align: center'>
				Etapa mas recurrente<br>{etapa_mas_frecuente} </h3><br>""",
				unsafe_allow_html=True
	)

with col4:
	## Tarjeta 4 - Cantidad de registros de la etapa mas recurrente
	st.markdown(f"""<h3 style=
				'color:#A6886D;
				background-color:#F7EBD6;
				border: 2px solid #A6886D;
				border-radius: 10px; padding: 10px;
				text-align: center'>
				Procesos en esta Etapa<br>{cant_etapa_mas_frecuente} </h3><br>""",
				unsafe_allow_html=True
	)

col5, col6 = st.columns(2)

with col5:
	st.subheader('Tipo delitos')
	tipo_delitos = df['DELITO'].value_counts()
	st.bar_chart(tipo_delitos)

with col6:
	st.subheader("Distribución por Departamentos")
	departamento = df['DEPARTAMENTO'].value_counts()
	fig = px.pie(
		names=departamento.index,  # Para los nombres de la Torta
		values=departamento.values # Para los valores de la Torta
	)
	fig.update_traces(textposition='outside', textinfo='percent+label')
	fig.update_layout(showlegend=False, height=350)
	st.plotly_chart(fig, key="torta_departamentos")
	

# Selección de dato para visualizar
cols_grafico = ['DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
df_grafico = df[cols_grafico]

st.subheader("Seleccione Dato a Visualizar")
variable = st.selectbox(
	'Seleccione la variable para el análisis:',
	options = df_grafico.columns
)

# st.subheader('Tipo delitos')
grafico = df_grafico[variable].value_counts()
st.bar_chart(grafico)

if st.checkbox('Mostrar Matriz de Datos'):
	st.subheader('Matriz de Datos')
	st.dataframe(df_grafico)

# Consulta por Fiscal Asignado
st.header('Consulta por Fiscal Asignado')
fiscal_consulta = st.selectbox(
	'Seleccione El Fiscal a Consultar:',
	options = df['FISCAL_ASIGNADO'].unique()
)

df_fiscal = df[df['FISCAL_ASIGNADO'] == fiscal_consulta]
st.dataframe(df_fiscal)

st.subheader(f'Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} Reportes')
st.subheader(f'{etapa_mas_frecuente} tiene {cant_etapa_mas_frecuente} registros')





max_cantidad_municipio = df2['MUNICIPIO_HECHOS'].value_counts().iloc[0]
st.write(f'# Eventos: {max_cantidad_municipio}') 

# CONTRUIR LA PÁGINA
st.set_page_config(page_title='Dashboard de Delitos - Fiscalia', layout='wide')
st.header('Dashboard de Delitos - Fiscalía')
#st.markdown(f"<center><h1>Dashboard de Delitos - Fiscalía</center>", unsafe_allow_html=True)

st.dataframe(DF2)

st.write(f'### Etapa más frecuente: {etapa_mas_frecuente} con {etapa_mas_frecuente} Eventos')
st.write(f'### {etapa_mas_frecuente} tiene {etapa_mas_frecuente} Eventos')

st.write(f'### Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} Eventos')
#st.write(f'### Cantidad de Eventos: {max_cantidad_municipio}')

st.subheader(f'Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} Eventos')
st.subheader(f'Etapa más frecuente: {etapa_mas_frecuente} con {etapa_mas_frecuente} Eventos')

st.subheader('Comportamiento Delitos')
delitos = df2['DELITO'].value_counts()
st.bar_chart(delitos)


import pandas as pd
import streamlit as st
import plotly.express as px

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

### Ejercicio 2

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

# 2