import streamlit as st
import joblib
import numpy as np
import shap
import matplotlib.pyplot as plt

# Load your pre-trained model
model = joblib.load('model.pkl')  # Update if your model is in a different path
explainer = shap.TreeExplainer(model)  # SHAP explainer for tree-based models

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
        # Make the prediction
        prediction = model.predict([features])
        st.write(f"Prediction: {prediction[0]}")
        
        # SHAP explanation (only for tree-based models like Random Forest, XGBoost, etc.)
        shap_values = explainer.shap_values([features])

        # Display SHAP summary plot (Feature Importance)
        st.subheader("Feature Importance (SHAP Values)")
        shap.summary_plot(shap_values, [features], feature_names=[f"Feature {i+1}" for i in range(8)])
        
        # Display individual SHAP value plot (Impact of each feature)
        st.subheader("SHAP Value for Each Feature")
        shap.initjs()
        st.pyplot(shap.force_plot(explainer.expected_value[0], shap_values[0], features))
        
    else:
        st.error("Please provide all 8 feature values.")





# Get feature importance from the model (for RandomForest or similar models)
importances = model.feature_importances_

# Plot the feature importance using Streamlit
st.subheader("Feature Importance (Bar Chart)")
plt.figure(figsize=(8, 6))
plt.barh([f"Feature {i+1}" for i in range(8)], importances)
plt.xlabel("Importance")
plt.title("Feature Importance")
st.pyplot(plt)
