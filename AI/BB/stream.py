import streamlit as st
import os 
import joblib
import numpy as np

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")


st.title("Bike Buyers Prediction App")

st.divider()

st.write("Please enter the following details and hit the predict button to get the buying prediction.")

st.divider()

income = st.number_input("Income", min_value = 10000, max_value=170000)
children = st.number_input("Children", min_value=0, max_value=5)
cars = st.number_input("Cars", min_value=0, max_value=4)
age = st.number_input("Age", min_value=0, max_value=90)
marital_status = st.selectbox("Marital Status", ["Married", "Single"])
gender = st.selectbox("Gender", ["Male", "Female"])
home_owner = st.selectbox("Gender", ["Yes", "No"])


st.divider()

predict_button = st.button("Predict")
st.divider()

if predict_button:
    
    gender_selected = 1 if gender == "Male" else 0
    home_owner_selected = 1 if home_owner == "Yes" else 0
    marital_status_selected = 1 if marital_status == "Married" else 0
    X = [income, children, cars, age, marital_status_selected, gender_selected, home_owner_selected]
    X1 = np.array(X)
    
    
    X_array = scaler.transform([X1])
    prediction = model.predict(X_array)[0]
    predicted = "Yes" if prediction == 1 else "No"
    st.snow()
    st.write(f"Predicted(Buyer): {predicted}")

else:
    st.write("Please fill in all the fields and click the predict button.")