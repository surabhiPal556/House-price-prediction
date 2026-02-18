import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("Random_search.pkl")

st.title("House Price Prediction")
st.markdown("---")

bedroom = st.number_input("Enter the number of bedroom", min_value=0, value=0)
bathroom = st.number_input("Enter the number of bathroom", min_value=0, value=0)
living_area = st.number_input("Enter the living area", min_value=0, value=2000)
condition_of_house = st.number_input("Condition of house", min_value=0, value=3)
number_of_school = st.number_input("School min value", min_value=0, value=0)

st.markdown("---")

prediction = st.button("Predict")

if prediction:
    # Create input array
    X_array = np.array([[bedroom, bathroom, living_area, condition_of_house, number_of_school]])

    # Predict
    pred = model.predict(X_array)

    # Extract value from array
    price = int(pred[0])

    st.write(f"House price = {price}")

else:
    st.write("Please click on the predict button")