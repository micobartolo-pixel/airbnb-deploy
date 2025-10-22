import streamlit as st
import pandas as pd
import joblib

# Carica il modello
model = joblib.load("airbnb_model.pkl")

# Titolo app
st.title("Previsione Prezzo Airbnb")

# Input utente
room_type = st.selectbox("Tipo di stanza", ["Entire home/apt", "Private room", "Shared room"])
minimum_nights = st.number_input("Numero minimo di notti", min_value=1, value=3)
number_of_reviews = st.number_input("Numero di recensioni", min_value=0, value=10)
availability_365 = st.number_input("Disponibilità annuale", min_value=0, value=200)

# Previsione
if st.button("Calcola prezzo"):
    input_data = pd.DataFrame([{
        "room_type": room_type,
        "minimum_nights": minimum_nights,
        "number_of_reviews": number_of_reviews,
        "availability_365": availability_365
    }])
    prediction = model.predict(input_data)[0]
    st.success(f"Prezzo previsto: €{prediction:.2f}")