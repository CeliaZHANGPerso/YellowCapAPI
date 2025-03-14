import fastapi
import uvicorn

from fastapi import FastAPI
from uvicorn import Config, Server
#from yellowcab.predict import predict

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

#@app.get("/predict")    
