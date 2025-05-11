import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity

teacher_vectors = np.load("teacher_vectors.npy", allow_pickle=True)
# Load saved models and data
scaler = joblib.load("scaler.pkl")
features = joblib.load("features.pkl")
data = pd.read_csv("original_teachers_df.csv")  # renamed from original_df

# Feature options
primary_subjects = sorted({col.split('_')[-1] for col in features if "Primary_Subject_" in col})
secondary_subjects = sorted({col.split('_')[-1] for col in features if "Secondary_Subject_" in col})
education_levels = sorted({col.split('_')[-1] for col in features if "Education_Level_" in col})
teaching_styles = sorted({col.split('_')[-1] for col in features if "Teaching_Style_" in col})
certifications = sorted({col.split('_')[-1] for col in features if "Certifications_" in col})
availabilities = sorted({col.split('_')[-1] for col in features if "Availability_" in col})
languages = sorted({col.split('_')[-1] for col in features if "Language_" in col})

# Streamlit UI
st.title("Teacher Recommendation System")

primary_subject = st.selectbox("Primary Subject", primary_subjects)
secondary_subject = st.selectbox("Secondary Subject", secondary_subjects)
education = st.selectbox("Education Level", education_levels)
teaching_style = st.selectbox("Teaching Style", teaching_styles)
certification = st.selectbox("Certification", certifications)
availability = st.selectbox("Availability", availabilities)
language = st.selectbox("Language", languages)
experience = st.slider("Years of Experience", 1, 30, 10)
rating = st.slider("Minimum Rating", 3.0, 5.0, 4.5)
courses = st.slider("Courses Taught", 5, 50, 20)
research_active = st.checkbox("Research Active", value=True)

# Scale input
input_data = pd.DataFrame([{
    "Years_of_Experience": experience,
    "Student_Rating": rating,
    "Courses_Taught": courses
}])
scaled_vals = scaler.transform(input_data)

# Build profile
course_profile = {
    f"Primary_Subject_{primary_subject}": 1,
    f"Secondary_Subject_{secondary_subject}": 1,
    f"Education_Level_{education}": 1,
    f"Teaching_Style_{teaching_style}": 1,
    f"Certifications_{certification}": 1,
    f"Availability_{availability}": 1,
    f"Language_{language}": 1,
    "Years_of_Experience": scaled_vals[0][0],
    "Student_Rating": scaled_vals[0][1],
    "Courses_Taught": scaled_vals[0][2],
    "Is_Research_Active": 1 if research_active else 0
}

query_vector = np.array([course_profile.get(f, 0) for f in features if f != "Teacher_ID"])
similarities = cosine_similarity([query_vector], teacher_vectors)
top_indices = similarities[0].argsort()[-5:][::-1]

# Show top matches
st.subheader("Top Recommended Teachers")
st.dataframe(data.iloc[top_indices][['Teacher_ID', 'Primary_Subject', 'Years_of_Experience', 'Student_Rating']])
