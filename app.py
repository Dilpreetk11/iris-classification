import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('knn_model.pkl')

# Set title
st.title("🌸 Iris Flower Species Prediction App")
st.markdown("Enter flower measurements to predict the species using KNN algorithm.")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.2)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3)

# Prepare input data
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    label_map = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    st.success(f"🌼 Predicted Species: **{label_map[prediction[0]]}**")
