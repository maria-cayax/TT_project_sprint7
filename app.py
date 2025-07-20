import pandas as pd
import plotly.express as px
import streamlit as st


st.header('Análisis de venta de vehículos usados')
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_lineplot = st.checkbox('Construir evolución de precio')

if build_lineplot:
    st.write('Evolución de precio según condición vehículo')

    df_car = car_data.groupby(['date_posted','condition'])['price'].mean().reset_index()
    fig_2= px.line(df_car, x="date_posted", y="price", color="condition",
              title= 'Precio promedio vehículos según día de pubicición')
    st.plotly_chart(fig_2, use_container_width=True)

