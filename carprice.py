import streamlit as st
import pickle
import pandas as pd
import numpy as np

with open('used_car_price_model.pkl', 'rb') as model_file:
    model_pipeline = pickle.load(model_file)

    st.title("Used Car Price Prediction")
    st.write("Enter car details to predict the price.")
    
    brand = st.selectbox("Select Brand", ['Toyota', 'Honda', 'Ford', 'BMW', 'Other'])
    model_year = st.number_input("Model Year", min_value=1990, max_value=2024, value=2015)
    milage = st.number_input("Mileage (in miles)", min_value=0, value=50000)
    fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Electric', 'Hybrid'])
    transmission = st.selectbox("Transmission Type", ['Automatic', 'Manual'])
    ext_col = st.selectbox("Exterior Color", ['Black', 'White', 'Gray', 'Other'])
    accident = st.radio("Accident History", ['Yes', 'No'])
    clean_title = st.radio("Clean Title", ['Yes', 'No'])
    
    input_data = pd.DataFrame({
        'brand': [brand],
        'model_year': [model_year],
        'milage': [milage],
        'fuel_type': [fuel_type],
        'transmission': [transmission],
        'ext_col': [ext_col],
        'accident': [accident],
        'clean_title': [clean_title]
    })
    
    if st.button("Predict Price"):
        predicted_price = model_pipeline.predict(input_data)[0]
        st.success(f"Estimated Price: ${predicted_price:,.2f}")


