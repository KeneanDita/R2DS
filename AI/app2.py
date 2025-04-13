import streamlit as st
import joblib
import numpy as np
import requests

# Load your pre-trained model
model = joblib.load('model.pkl')  # Update if your model is in a different path

# Streamlit UI
st.title("ML Model Prediction Interface")
st.write("Enter 8 feature values to get a prediction:")

# Input fields for each of the 8 features
feature_1 = st.number_input("Feature 1", value=0.5)
feature_2 = st.number_input("Feature 2", value=1.2)
feature_3 = st.number_input("Feature 3", value=3.1)
feature_4 = st.number_input("Feature 4", value=4.7)
feature_5 = st.number_input("Feature 5", value=2.0)
feature_6 = st.number_input("Feature 6", value=3.3)
feature_7 = st.number_input("Feature 7", value=0.8)
feature_8 = st.number_input("Feature 8", value=1.5)

# Create a button to trigger the prediction
if st.button("Predict"):
    # Collect the features into a list
    features = [feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7, feature_8]
    
    # Ensure the number of features is correct
    if len(features) == 8:
        prediction = model.predict([features])
        st.write(f"Prediction: {prediction[0]}")
    else:
        st.error("Please provide all 8 feature values.")
