import pickle
from yellowcab.src.utils import transform_input 

def predict_duration(input, path_model="yellowcab/model/forest_model.pkl") -> int:
    model = pickle.load(open(path_model, 'rb'))
    transformed_input = transform_input(input)
    prediction = model.predict(transformed_input)
    return prediction

from yellowcab.src.utils import ModelPredictIn

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

print(inputs.extra)