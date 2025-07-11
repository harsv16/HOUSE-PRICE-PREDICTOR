import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')
features = joblib.load('features.pkl')

st.title("🏠 House Price Prediction App")

st.markdown("Enter the house details to estimate the price:")

user_input = []
for feature in features:
    val = st.number_input(f"{feature}", step=1.0)
    user_input.append(val)

if st.button("Predict"):
    prediction = model.predict([user_input])[0]
    st.success(f"Estimated House Price: ₹ {prediction:,.2f}")
