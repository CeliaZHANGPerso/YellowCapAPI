import pickle
import pandas as pd
from yellowcab.src.utils import transform_input_post, transform_input_get 

def predict_duration_post(input, path_model="yellowcab/model/forest_model.pkl") -> int:
    model = pickle.load(open(path_model, 'rb'))
    dv = pickle.load(open("yellowcab/model/forest_dv.pkl", 'rb'))
    transformed_input = transform_input_post(input, dv)
    prediction = model.predict(transformed_input)
    return prediction

def predict_duration_get(
        VendorID: int,
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
        airport_fee: float,
        path_model="yellowcab/model/forest_model.pkl") -> int:
    input_dict = {
        "VendorID": [VendorID],
        "passenger_count": [passenger_count],
        "trip_distance": [trip_distance],
        "RatecodeID": [RatecodeID],
        "store_and_fwd_flag": [store_and_fwd_flag],
        "PULocationID": [PULocationID],
        "DOLocationID": [DOLocationID],
        "payment_type": [payment_type],
        "fare_amount": [fare_amount],
        "extra": [extra],
        "mta_tax": [mta_tax],
        "tip_amount": [tip_amount],
        "tolls_amount": [tolls_amount],
        "improvement_surcharge": [improvement_surcharge],
        "total_amount": [total_amount],
        "congestion_surcharge": [congestion_surcharge],
        "airport_fee": [airport_fee]
    }
    print(input_dict)

    input_df = pd.DataFrame.from_dict(input)
    print(input_df)
    model = pickle.load(open(path_model, 'rb'))
    dv = pickle.load(open("yellowcab/model/forest_dv.pkl", 'rb'))
    transformed_input = transform_input_get(input_df, dv)
    prediction = model.predict(transformed_input)
    return prediction

 