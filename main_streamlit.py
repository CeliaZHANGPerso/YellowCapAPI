import streamlit as st
import pandas as pd
import numpy as np
import requests

st.title("Yellow Cab")
st.header("Estimate the duration")
st.markdown("Enter your variables to get the prediction")

st.number_input("VendorID", value=1)
st.number_input("passenger_count", value=1)
st.number_input("trip_distance", value=2.1)
st.number_input("RatecodeID", value=1)
st.text_input("store_and_fwd_flag", value="N")
st.number_input("PULocationID", value=142)
st.number_input("DOLocationID", value=43)
st.number_input("payment_type", value=2)
st.number_input("fare_amount", value=8.0)
st.number_input("extra", value=3.0)
st.number_input("mta_tax", value=0.5)
st.number_input("tip_amount", value=0.0)
st.number_input("tolls_amount", value=0.0)
st.number_input("improvement_surcharge", value=0.3)
st.number_input("total_amount", value=11.8)
st.number_input("congestion_surcharge", value=2.5)
st.number_input("airport", value=0)

data = {
    "VendorID": 1,
    "passenger_count": 1,
    "trip_distance": 2.1,
    "RatecodeID": 1,
    "store_and_fwd_flag": "N",
    "PULocationID": 142,
    "DOLocationID": 43,
    "payment_type": 2,
    "fare_amount": 8.0,
    "extra": 3.0,
    "mta_tax": 0.5,
    "tip_amount": 0.0,
    "tolls_amount": 0.0,
    "improvement_surcharge": 0.3,
    "total_amount": 11.8,
    "congestion_surcharge": 2.5,
    "airport_fee": 0
}
BASE_URL =  'https://yellowcapapi-609285842864.europe-west9.run.app'
if st.button("Predict"):
    result = requests.get(f"{BASE_URL}/predict_get/", params=data)
    st.write(result.json())
