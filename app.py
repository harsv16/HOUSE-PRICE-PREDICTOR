import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="House Price Predictor", page_icon="🏡")
st.title("🏡 House Price Prediction App")

# Input fields
location = st.selectbox("Select Location", ["Mumbai", "Bengaluru", "Delhi", "Pune", "Hyderabad"])
area = st.number_input("Area (in sqft)", min_value=300)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
age = st.slider("Age of the Property (years)", 0, 50)

# Predict button
if st.button("Predict Price"):
    data = {
        "Location": [location],
        "Area (sqft)": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Age": [age]
    }
    import pandas as pd
    input_df = pd.DataFrame(data)
    prediction = model.predict(input_df)
    st.success(f"Estimated House Price: ₹ {round(prediction[0], 2)} lakhs")
