from pydantic import BaseModel
from typing import List
import pandas as pd

class ModelPredictIn(BaseModel):
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

def transform_input(inputs: ModelPredictIn) -> pd.DataFrame:
    # Transform input into a format that can be fed into the model
    #df = pd.DataFrame(dict(inputs))
    df = pd.DataFrame(inputs.model_dump())
    df = encode_categorical_cols(df)
    return df


inputs = ModelPredictIn(
    passenger_count=1,
    trip_distance=2.1,
    RatecodeID=1,
    store_and_fwd_flag="N",
    PULocationID=142,
    DOLocationID=43,
    payment_type=2,
    fare_amount=10.0,
    extra=3,
    mta_tax=0.5,
    tip_amount=0.0,
    tolls_amount=0.0,
    improvement_surcharge=0.3,
    total_amount=11.3,
    congestion_surcharge=2.5,
    airport_fee=0.0
)

print()
print(transform_input(inputs))
