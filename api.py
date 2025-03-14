from fastapi import FastAPI
from typing import List   
from yellowcab.predict import predict_duration, ModelPredictIn

app = FastAPI()

@app.get("/home")
def read_root():
    return {"Hello": "World"}

@app.post("/predict", response_model=List[ModelPredictIn])  
def predict(input: List[ModelPredictIn]):
    return predict_duration(input)  



