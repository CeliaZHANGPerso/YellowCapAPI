from pydantic import BaseModel
from typing import List
import pandas as pd

class ModelPredictIn(BaseModel):
    trip_distance: float
    total_amount: float
    payment_type: int
    trip_type: int                  
    rate_code: int
    extra: float
    tolls_amount: float
    mta_tax: float
    improvement_surcharge: float
    congestion_surcharge: float
    pickup_month: int
    pickup_day: int
    pickup_weekday: int
    pickup_hour: int
    pickup_minute: int
    dropoff_month: int
    dropoff_day: int
    dropoff_weekday: int
    dropoff_hour: int
    dropoff_minute: int

def filter_outliers(df: pd.DataFrame, min_duration: int = 1, max_duration: int = 60) -> pd.DataFrame:
    return df[df["duration"].between(min_duration, max_duration)]

def encode_categorical_cols(df: pd.DataFrame, categorical_cols: List[str] = None) -> pd.DataFrame:
    if categorical_cols is None:
        categorical_cols = ["PULocationID", "DOLocationID", "passenger_count"]
    df[categorical_cols] = df[categorical_cols].fillna(-1).astype("int")
    df[categorical_cols] = df[categorical_cols].astype("str")
    return df

def transform_input(inputs: ModelPredictIn) -> pd.DataFrame:
    # Transform input into a format that can be fed into the model
    df = pd.DataFrame(inputs, index=[0])
    df = filter_outliers(df)
    df = encode_categorical_cols(df)
    return df







