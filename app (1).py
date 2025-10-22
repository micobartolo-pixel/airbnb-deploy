import streamlit as st
import pandas as pd
import joblib

# Carica il modello
model = joblib.load("airbnb_model.pkl")

# Titolo
st.title("💰 Airbnb Price Prediction")

# Input utente
room_type = st.selectbox("Tipo di stanza", ["Entire home/apt", "Private room", "Shared room"])
minimum_nights = st.number_input("Notti minime", min_value=1, value=3)
number_of_reviews = st.number_input("Numero di recensioni", min_value=0, value=10)
availability_365 = st.number_input("Disponibilità annuale (365 giorni)", min_value=0, max_value=365, value=180)

# Crea dataframe per la predizione
input_data = pd.DataFrame({
    "room_type": [room_type],
    "minimum_nights": [minimum_nights],
    "number_of_reviews": [number_of_reviews],
    "availability_365": [availability_365]
})

# Encoding manuale per 'room_type'
room_type_map = {
    "Entire home/apt": 0,
    "Private room": 1,
    "Shared room": 2
}
input_data["room_type"] = input_data["room_type"].map(room_type_map)

# Predizione
if st.button("Prevedi Prezzo"):
    prediction = model.predict(input_data)[0]
    st.success(f"💵 Prezzo stimato: {round(prediction, 2)} €")