import streamlit as st


st.header('XGBoost model')
st.write('Learn what an XGBoost model is and how to use it.')
st.video('https://www.youtube.com/watch?v=OtD8wVaFm6E')

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.sidebar.header('This is a sidebar header')
st.sidebar.write('This is a sidebar line')
st.sidebar.table({'Col1': [1, 2], 'Col2': [3, 4]})