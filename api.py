from fastapi import FastAPI
from typing import List   
from yellowcab.src.utils import ModelPredictIn
from yellowcab.src.predict import predict_duration_post, predict_duration_get

app = FastAPI()

@app.get("/home")
def read_root():
    return {"Hello": "World"}

@app.post("/predict_post/", response_model=float)  
def predict_post(input: List[ModelPredictIn]): # random forest regressor model
    return predict_duration_post(input)

@app.get("/predict_get/")
def predict_get(VendorID: int, 
            passenger_count: int, 
            trip_distance: float, 
            RatecodeID: int, 
            store_and_fwd_flag: str, 
            PULocationID: int, 
            DOLocationID:int,
            payment_type: int,
            fare_amount: float,
            extra: float,
            mta_tax: float,
            tip_amount: float,
            tolls_amount: float,
            improvement_surcharge: float,
            total_amount: float,
            congestion_surcharge: float,
            airport_fee: float):
    return predict_duration_get(
        VendorID,
        passenger_count,
        trip_distance,
        RatecodeID,
        store_and_fwd_flag,
        PULocationID,
        DOLocationID,
        payment_type,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        improvement_surcharge,
        total_amount,
        congestion_surcharge,
        airport_fee)

