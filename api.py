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
    return(float(predict_duration_post(input)[0]))

# @app.get("/predict/")
# def predict(name:str):
#     return {"Hello": name}

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
        airport_fee
    )   
    # duration = predict_duration_get(VendorID, 
    #         passenger_count, 
    #         trip_distance, 
    #         RatecodeID, 
    #         store_and_fwd_flag, 
    #         PULocationID, 
    #         DOLocationID,
    #         payment_type,
    #         fare_amount,
    #         extra,
    #         mta_tax,
    #         tip_amount,
    #         tolls_amount,
    #         improvement_surcharge,
    #         total_amount,
    #         congestion_surcharge,
    #         airport_fee)
    # input_df["VendorID"] = VendorID
    # input_df["passenger_count"] = passenger_count
    # input_df["trip_distance"] = trip_distance
    # input_df["RatecodeID"] = RatecodeID
    # input_df["store_and_fwd_flag"] = store_and_fwd_flag
    # input_df["PULocationID"] = PULocationID
    # input_df["DOLocationID"] = DOLocationID
    # input_df["payment_type"] = payment_type
    # input_df["fare_amount"] = fare_amount
    # input_df["extra"] = extra
    # input_df["mta_tax"] = mta_tax
    # input_df["tip_amount"] = tip_amount
    # input_df["tolls_amount"] = tolls_amount
    # input_df["improvement_surcharge"] = improvement_surcharge
    # input_df["total_amount"] = total_amount
    # input_df["congestion_surcharge"] = congestion_surcharge
    # input_df["airport_fee"] = airport_fee
    return duration

