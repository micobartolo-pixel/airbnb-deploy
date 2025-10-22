import streamlit as st
import pandas as pd
import joblib

# Carica il modello
model = joblib.load("airbnb_model.pkl")

st.title("💸 Airbnb Price Predictor")
st.write("Inserisci le caratteristiche dell'annuncio per stimare il prezzo:")

# Input utente
room_type = st.selectbox("Tipo di stanza", ["Entire home/apt", "Private room", "Shared room"])
minimum_nights = st.number_input("Notti minime", min_value=1, value=3)
number_of_reviews = st.number_input("Numero di recensioni", min_value=0, value=10)
availability_365 = st.slider("Disponibilità (giorni l'anno)", 0, 365, 180)

# Mappa room_type a numeri se necessario
room_type_map = {"Entire home/apt": 0, "Private room": 1, "Shared room": 2}
room_type_encoded = room_type_map[room_type]

# Costruisci il dataframe di input
input_data = pd.DataFrame({
    "room_type": [room_type_encoded],
    "minimum_nights": [minimum_nights],
    "number_of_reviews": [number_of_reviews],
    "availability_365": [availability_365]
})

# Predizione
if st.button("💡 Prevedi il prezzo"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Prezzo stimato: {prediction:.2f}€")