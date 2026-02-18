import streamlit as st
import numpy as np
from joblib import load   # ✅ fixed import

# Load model safely
@st.cache_resource
def load_model():
    return load("Random_search.pkl")

model = load_model()

# UI
st.title("🏠 House Price Prediction")
st.markdown("---")

# Inputs
bedroom = st.number_input("Enter number of bedrooms", min_value=0, value=1)
bathroom = st.number_input("Enter number of bathrooms", min_value=0, value=1)
living_area = st.number_input("Enter living area", min_value=0, value=2000)
condition_of_house = st.number_input("Condition of house", min_value=0, value=3)
number_of_school = st.number_input("Number of nearby schools", min_value=0, value=1)

st.markdown("---")

# Button
if st.button("Predict"):
    try:
        # Prepare input
        X_array = np.array([[bedroom, bathroom, living_area, condition_of_house, number_of_school]])

        # Prediction
        pred = model.predict(X_array)

        # Result
        price = int(pred[0])

        st.success(f"Estimated House Price = {price}")

    except Exception as e:
        st.error("Error in prediction. Please check inputs.")
        st.write(e)

else:
    st.info("Click the Predict button to get house price")
