import pandas as pd
import plotly.express as px
import scipy.stats as sts
import streamlit as st

cars = pd.read_csv('vehicles_us.csv')
PLOT_TYPES=("Histogram", "Scatter")


st.title('Vehicles Analysis')

st.header('Exploratory data Analysis')

variable = st.selectbox("What variable would you like to analyze", cars.columns)
plots_report = []

st.subheader('Now selected: '+variable)
st.write(plots_report)

plot_type = st.selectbox('Please add type of graph', PLOT_TYPES)

if plot_type=="Histogram":
    fig = px.histogram(cars, x=variable)
elif plot_type=="Scatter":
    st.write('Please choose y')
    car_columns_filtered = list(cars.columns)

    index_variable = car_columns_filtered.index(variable)
    car_columns_filtered.pop(index_variable)

    scatter_y = st.selectbox("What variable would you like to analyze", car_columns_filtered)
    fig = px.scatter(cars, x=variable, y=scatter_y)
elif plot_type=="Lineplot":
    fig = st.line_chart(cars, x=variable)

add_plot = st.button('Add plot')

if add_plot:
    plots_report.append(fig)
    st.plotly_chart(fig)







