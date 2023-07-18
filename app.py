import streamlit as st
from predict import show_predict_page
from graphs import show_graph_page
from general import show_general_page

page = st.sidebar.selectbox("Options", ("Predict", "Graphs","General Informatics"))
if page == "Graphs":
    show_graph_page()
elif page == "Predict":
    show_predict_page()
elif page == "General Informatics":
    show_general_page()
