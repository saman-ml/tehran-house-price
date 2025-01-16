import streamlit as st
from utils import address_list

import pandas as pd
import joblib

model = joblib.load('model.joblib')
st.title('Tehran House Price in 1400 :house_buildings:')
area = st.number_input('Input House Area', 45,1000)
room = st.slider("Choose Room",0,10)
parking = st.selectbox("Parking", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
warehouse = st.selectbox("Warehouse", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
elevator = st.selectbox("Elevator", options=[0, 1], format_func=lambda x: "Yes" if x else "No")
address = st.selectbox("Select Address", address_list)

if st.button("Predict Price"):
    user_data = pd.DataFrame({
        'Area': [area],
        'Room': [room],
        'Parking': [parking],
        'Warehouse': [warehouse],
        'Elevator': [elevator]
    })

    for col in address_list:
        user_data[col] = 0
    user_data[address] = 1

    prediction = model.predict(user_data)[0]

    st.write(f"### Predicted Price: {prediction:,.0f} TMN")