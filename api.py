from fastapi import FastAPI
from typing import List   
from yellowcab.src.utils import ModelPredictIn
from yellowcab.src.predict import predict_duration

app = FastAPI()

@app.get("/home")
def read_root():
    return {"Hello": "World"}

@app.post("/predict/", response_model=int)  
def predict(input: List[ModelPredictIn]): # random forest regressor model
    return predict_duration(input)  



