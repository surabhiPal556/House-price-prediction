import streamlit as st
import numpy as np
from joblib import load

# Load trained model
model = load("Random_search.pkl")

# Title
st.title("🏠 House Price Prediction App")

st.write("Enter details to predict house price")

# Inputs
area = st.number_input("Area (in square feet)", min_value=500, max_value=10000, step=50)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
stories = st.number_input("Number of Floors", min_value=1, max_value=5, step=1)
parking = st.number_input("Parking Spaces", min_value=0, max_value=5, step=1)

# Convert inputs to array
input_data = np.array([[area, bedrooms, bathrooms, stories, parking]])

# Prediction button
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹ {int(prediction[0])}")

