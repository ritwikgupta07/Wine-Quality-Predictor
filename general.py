import streamlit as st
import pickle
import numpy as np
import pandas as pd


def show_general_page():
    st.title("General Informatics")
    st.write("Provide information for prediction")

    st.subheader('\n\nFixed Acidity')
    st.write("""The level of non-volatile acids in wine, such as tartaric, malic, and citric acids. Fixed acidity is 
             important for wine's flavor profile, with higher levels contributing to a more tart and acidic taste. It is measured in g/L.""")

    st.subheader('\n\nVolatile Acidity')
    st.write("""The volatile organic acids that can affect the wine's aroma and flavor, such as acetic acid. High levels of volatile acidity 
             can give a wine an unpleasant "vinegary" taste, while lower levels contribute to the wine's overall balance and complexity. It is measured in g/L.""")

    st.subheader('\n\nCitric Acid')
    st.write("""Citric acid in wine is one of the types of fixed acids present in the wine, along with tartaric and malic acids. It provides 
             freshness and adds a tart, tangy flavor to the wine. It is measured in g/L.""")

    st.subheader('\n\nResidual Sugar')
    st.write("""Residual sugar refers to the amount of unfermented sugar left in the wine after the winemaking process. It affects the 
             wine's sweetness level, with higher residual sugar levels resulting in a sweeter wine and lower levels resulting in a drier wine. It is measured in g/L.""")
    
    st.subheader('\n\nChlorides')
    st.write("""The concentration of chloride ions is generally indicative of the presence of sodium chloride. They may have a key role on a potential salty taste of a wine. It is measured in g/L.""")

    st.subheader('\n\nFree Sulfur Dioxide')
    st.write("""Free sulfur dioxide is a type of sulfur compound that acts as a preservative, protecting the wine from spoilage and oxidation. Too much sulfur 
             dioxide can give a wine an unpleasant, bitter taste, while too little can result in spoilage and an off-flavor. It is measured in mg/L.""")

    st.subheader('\n\nTotal Sulfur Dioxide')
    st.write("""Total sulfur dioxide in wine refers to the sum of both the bound and free forms of sulfur dioxide in the wine. 
             It is an important factor in wine preservation, but high levels can impact the wine's flavor and aroma. It is measured in mg/L.""")

    st.subheader('\n\nDensity')
    st.write("""The weight of wine compared to its volume. Density can be used to determine the alcohol content of wine, with 
             higher density indicating a higher alcohol content. It is measured in g/cc.""")

    st.subheader('\n\npH of the wine')
    st.write("""A measure of the wine's acidity or alkalinity, with a pH range of 3-4 considered ideal for most wines. A lower 
             pH indicates a higher acidity, while a higher pH indicates a less acidic wine. It is measured on the scale of 0 to 14.""")

    st.subheader('\n\nSulphates')
    st.write("""Sulfates in wine are a natural byproduct of fermentation and can also be added as a preservative. Higher levels 
             of sulphates can result in a bitter taste, while lower levels can lead to a smoother and gentler flavor profile. It is measured in g/L.""")

    st.subheader('\n\nAlcoholic content of the wine')
    st.write("""The amount of ethanol in wine, which is produced through fermentation. Alcohol contributes to the wine's body, flavor, 
             and overall strength, with higher alcohol content resulting in a stronger and more flavorful wine. It is measured in volume percentage.""")
