import pandas as pd
import streamlit as st
import plotly.express as px
import os



path = os.path.dirname(__file__)
data = path+'/USA_cars_datasets.csv'
data = pd.DataFrame()
data2 = []
data2 = data.copy()
data2 = pd.DataFrame()

hist_1 = px.histogram(data2,x="price")
st.plotly_chart(hist_1, use_container_width=True)

hist_2 = px.histogram(data2,x="year")
st.plotly_chart(hist_2, use_container_width=True)

hist_3 = px.histogram(data2,x="mileage")
st.plotly_chart(hist_3, use_container_width=True)

hist_4 = px.histogram(data2,x="lot")
st.plotly_chart(hist_4, use_container_width=True)


sct_1 = px.scatter(data2, x="year", y="lot")
st.plotly_chart(sct_1, use_container_width=True)


sct_2 = px.scatter(data2, x="year", y="price")
st.plotly_chart(sct_2, use_container_width=True)


sct_3 = px.scatter(data2, x="year", y="mileage")
st.plotly_chart(sct_3, use_container_width=True)


agree = st.checkbox('Show me year and mileage scatter plot')

if agree:
    st.plotly_chart(sct_3, use_container_width=True)
