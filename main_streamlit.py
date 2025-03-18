import streamlit as st 
import requests
import pickle
import os
import loguru

BACKEND_URL = os.getenv("BACKEND_URL")
loguru.logger.info(f'BACKEND_URL: {BACKEND_URL}')

st.markdown("# Yellowcab Prediction")
st.markdown("### Predict the duration of the rip")
st.markdown("#### Input the following details to predict the duration of the trip")

VendorID = st.number_input("VendorID", value=1)
passenger_count = st.number_input("passenger_count", value=1)
trip_distance = st.number_input("trip_distance", value=2.1)
RatecodeID = st.number_input("RatecodeID", value=1)
store_and_fwd_flag = st.text_input("store_and_fwd_flag", value="N")        
PULocationID = st.number_input("PULocationID", value=142)
DOLocationID = st.number_input("DOLocationID", value=43)
payment_type = st.number_input("payment_type", value=2)
fare_amount = st.number_input("fare_amount", value=8)
extra = st.number_input("extra", value=3)
mta_tax = st.number_input("mta_tax", value=0.5)
tip_amount = st.number_input("tip_amount", value=0)
tolls_amount = st.number_input("tolls_amount", value=0)
improvement_surcharge = st.number_input("improvement_surcharge", value=0.3)
total_amount = st.number_input("total_amount", value=11.8)
congestion_surcharge = st.number_input("congestion_surcharge", value=2.5)
airport_fee = st.number_input("airport_fee", value=0)

data = {"VendorID": VendorID,
        "passenger_count": passenger_count,
        "trip_distance": trip_distance,
        "RatecodeID": RatecodeID,
        "store_and_fwd_flag": store_and_fwd_flag,
        "PULocationID": PULocationID,
        "DOLocationID": DOLocationID,
        "payment_type": payment_type,
        "fare_amount": fare_amount,
        "extra": extra,
        "mta_tax": mta_tax,
        "tip_amount": tip_amount,
        "tolls_amount": tolls_amount,
        "improvement_surcharge": improvement_surcharge,
        "total_amount": total_amount,
        "congestion_surcharge": congestion_surcharge,
        "airport_fee": airport_fee}

if st.button("Predict"):
    url = BACKEND_URL + "predict_get/"
    loguru.logger.info(f'BACKEND_URL: {BACKEND_URL}')
    response = requests.get(url, params = data) 
    result = response.json()
    st.markdown(f"Predicted duration of the trip is {result}")
