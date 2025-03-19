from pydantic import BaseModel
from typing import List
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from datetime import datetime

class ModelPredictIn(BaseModel):
    VendorID: int
    passenger_count: int
    trip_distance: float
    RatecodeID: int
    store_and_fwd_flag: str
    PULocationID: int
    DOLocationID:int
    payment_type: int
    fare_amount: float
    extra: float
    mta_tax: float
    tip_amount: float
    tolls_amount: float
    improvement_surcharge: float
    total_amount: float
    congestion_surcharge: float
    airport_fee: float


def encode_categorical_cols(df: pd.DataFrame, categorical_cols: List[str] = None) -> pd.DataFrame:
    if categorical_cols is None:
        categorical_cols = ["PULocationID", "DOLocationID", "passenger_count"]
    df[categorical_cols] = df[categorical_cols].fillna(-1).astype("int")
    df[categorical_cols] = df[categorical_cols].astype("str")
    return df

def extract_x_y(
    df: pd.DataFrame,
    categorical_cols: List[str] = None,
    dv: DictVectorizer = None,
    with_target: bool = True,
) -> dict:

    if categorical_cols is None:
        categorical_cols = ["PULocationID", "DOLocationID", "passenger_count"]
    dicts = df[categorical_cols].to_dict(orient="records")

    y = None
    if with_target:
        if dv is None:
            dv = DictVectorizer()
            dv.fit(dicts)
        y = df["duration"].values

    x = dv.transform(dicts)
    return x, y, dv

def transform_input_post(inputs: ModelPredictIn, dv: DictVectorizer) -> float:
    # Transform input into a format that can be fed into the model
    inputs = {k: [v] for k, v in inputs[0].__dict__.items()}
    df = pd.DataFrame(inputs, index=[0])
    print("1")
    df = encode_categorical_cols(df)
    print("2")
    x, _, dv = extract_x_y(df, dv=dv, with_target=False)
    print(x)
    return x

def transform_input_get(input_df, dv:DictVectorizer) -> float:
    # Transform input into a format that can be fed into the model
    print("3")
    df = encode_categorical_cols(input_df)
    print("4")
    x, _, dv = extract_x_y(df, dv=dv, with_target=False)
    print(x)
    return x
