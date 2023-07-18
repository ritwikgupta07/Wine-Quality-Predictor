import streamlit as st
import pickle
import numpy as np
import pandas as pd

# st.set_page_config(page_title="Predict")


def load_model():
    with open("prediction_model", 'rb') as file:
        ld_model = pickle.load(file)
    return ld_model


data = load_model()
model = data["model"]
scaler = data["scaler"]


def show_predict_page():
    st.title("Wine Quality Prediction")
    st.write("Provide information for prediction\n")

    fixed_acidity = st.slider("\nFixed Acidity (in g/L)", 4.0, 13.0)
    volatile_acidity = st.slider("\nVolatile Acidity (in g/L)", 0.10, 1.1)
    citric_acid = st.slider("\nCitric Acid (in g/L)", 0.0, 0.8)
    # residual_sugar = st.slider("\nResidual Sugar (in g/L)", 0.5, 4.0)
    chlorides = st.slider("\nChlorides (in g/L)", 0.000, 0.120)
    # free_sulfur_dioxide = st.slider("\nFree Sulfur Dioxide (in mg/L)", 0, 42)
    total_sulfur_dioxide = st.slider(
        "\nTotal Sulfur Dioxide (in mg/L)", 6, 122)
    density = st.slider("\nDensity (in g/cc)", 0.97, 1.10)
    # pH = st.slider("\npH of the Wine", 2.9, 3.7)
    sulphates = st.slider("\nSulphates (in g/L)", 0.3, 1.0)
    alcohol = st.slider("\nAlcohol Content (in %)", 8.0, 14.0)
    st.subheader("\n\n")
    ok = st.button("Predict Quality")
    if ok:
        test = pd.read_csv(
            'tester.csv')

        # X = np.array([[, , , , ,
        #              , , , , , ]])

        dic = {'fixed acidity': [fixed_acidity], 'volatile acidity': [volatile_acidity], 'citric acid': [citric_acid], 'chlorides': [
            chlorides], 'total sulfur dioxide': [total_sulfur_dioxide], 'density': [density], 'sulphates': [sulphates], 'alcohol': [alcohol]}
        newent = pd.DataFrame(dic)
        test = pd.concat([test, newent], axis=0)
        testsc = scaler.fit_transform(test)
        y = model.predict([testsc[-1]])
        if y == 0:
            st.subheader("The Wine is of Bad Quality")
        elif y == 1:
            st.subheader("The Wine is of Good Quality")
