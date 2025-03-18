import requests
url = "http://127.0.0.1:8000/predict_get/" #BACKEND_URL 

data = {
    "VendorID": 1,
    "tpep_pickup_datetime": "2025-03-14T17:44:03.462Z",
    "tpep_dropoff_datetime": "2025-03-14T17:50:03.462Z",
    "passenger_count": 1,
    "trip_distance": 2.1,
    "RatecodeID": 1,
    "store_and_fwd_flag": "N",
    "PULocationID": 142,
    "DOLocationID": 43,
    "payment_type": 2,
    "fare_amount": 8.0,
    "extra": 3.0,
    "mta_tax": 0.5,
    "tip_amount": 0,
    "tolls_amount": 0,
    "improvement_surcharge": 0.3,
    "total_amount": 11.8,
    "congestion_surcharge": 2.5,
    "airport_fee": 0
  }




response = requests.get(url, params = data) 
result = response.json()
print(result)