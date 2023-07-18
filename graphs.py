import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image


# st.set_page_config(page_title="Graphs")
def show_graph_page():
    st.title("Visual Information for deep understanding")
    st.write("Here you can get some graphical and data info regarding our data set\n")

    tab = pd.read_csv('winequality-red.csv')
    st.dataframe(tab)

    bins = (8, 9.5, 10.5, 11.5, 12.5, 13.5, 14)
    labels = ["8", "9", "10", "11", "12", "13"]
    tab['alcohol2'] = pd.cut(x=tab['alcohol'], bins=bins, labels=labels)
    tab

    alcohol = tab["alcohol"].unique().tolist()
    sulphates = tab["sulphates"].unique().tolist()
    alcohol2 = tab["alcohol2"].unique().tolist()
    quality = tab["quality"].unique().tolist()

    alcohol_selection = st.slider("Alcohol content: ", min_value=min(
        alcohol), max_value=max(alcohol), value=(min(alcohol), max(alcohol)))

    # alcohol_selection = st.multiselect("Alcohol: ", alcohol, default=alcohol)
    quality_selection = st.multiselect("Quality: ", quality, default=quality)

    mask = (tab["alcohol"].between(*alcohol_selection)
            ) & (tab["quality"].isin(quality_selection))
    numofresult = tab[mask].shape[0]

    st.markdown(f'Available result: {numofresult}')

    grouped = tab[mask].groupby(by="quality").count()[["alcohol"]]
    grouped = grouped.rename(columns={"Alcohol Content": "Quality"})
    grouped = grouped.reset_index()

    bar_chart = px.bar(grouped, x="quality", y="alcohol", text="alcohol", color_discrete_sequence=[
                       '#F63366']*len(grouped), template='plotly_white')
    st.plotly_chart(bar_chart)

    sulphate_selection = st.slider("Sulphates content: ", min_value=min(
        sulphates), max_value=max(sulphates), value=(min(sulphates), max(sulphates)))
    # alcohol_selection = st.multiselect("Alcohol: ", alcohol, default=alcohol)
    # quality_selection2 = st.multiselect("Quality: ", quality, default=quality)

    mask2 = (tab["sulphates"].between(*sulphate_selection)
             ) & (tab["quality"].isin(quality_selection))
    numofresult2 = tab[mask2].shape[0]

    st.markdown(f'Available result: {numofresult2}')

    grouped2 = tab[mask2].groupby(by="quality").count()[["sulphates"]]
    grouped2 = grouped2.rename(columns={"Sulphate Content": "Quality"})
    grouped2 = grouped2.reset_index()

    bar_chart2 = px.bar(grouped2, x="quality", y="sulphates", text="sulphates", color_discrete_sequence=[
        '#F63366']*len(grouped2), template='plotly_white')
    st.plotly_chart(bar_chart2)

    pie_chart = px.pie(tab, title="Dependence of quality on alcohol content",
                       values="alcohol2", names="quality")
    st.plotly_chart(pie_chart)
