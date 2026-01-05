#Project
import streamlit as st
import numpy as np
import pandas as pd
from xgboost import XGBClassifier

@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
    cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
            'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
    return pd.read_csv(url, names=cols)

df = load_data()

@st.cache_resource
def train_model(data):
    X = data.drop("Outcome", axis=1)
    y = data["Outcome"]
    model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
    model.fit(X, y)
    return model

model = train_model(df)

st.title("Diabetes Prediction App")
st.write("This app predicts whether a person has diabetes based on medical input parameters.")

pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=140, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.372, format="%.3f")
age = st.number_input("Age", min_value=0, max_value=120, value=33)

if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)[0][1]

    if prediction[0] == 1:
        st.error(f"Prediction: Positive (Diabetic) with probability {proba:.2f}")
    else:
        st.success(f"Prediction: Negative (Non-Diabetic) with probability {proba:.2f}")
