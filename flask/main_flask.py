from flask import request, Flask, render_template
import requests
import logging
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Yellow Cab Prediction API"

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        VendorID = request.form['VendorID']
        passenger_count = request.form['passenger_count']
        trip_distance = request.form['trip_distance']
        RatecodeID = request.form['RatecodeID']
        store_and_fwd_flag = request.form['store_and_fwd_flag']
        PULocationID = request.form['PULocationID']
        DOLocationID = request.form['DOLocationID']
        payment_type = request.form['payment_type']
        fare_amount = request.form['fare_amount']
        extra = request.form['extra']
        mta_tax = request.form['mta_tax']
        tip_amount = request.form['tip_amount']
        tolls_amount = request.form['tolls_amount']
        improvement_surcharge = request.form['improvement_surcharge']
        total_amount = request.form['total_amount']
        congestion_surcharge = request.form['congestion_surcharge']
        airport_fee = request.form['airport_fee']

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
        BASE_URL =  'http://fastapi:8002'
        prediction = requests.get(f'{BASE_URL}/predict_get/', params=input_dict)
        print(prediction.json())
        return render_template('predict.html', prediction=prediction.json())
    return render_template('predict.html')


if __name__ == "__main__":
    logger = logging.getLogger('werkzeug')
    logger.info(f'Starting the Flask API on PORT {os.environ.get("PORT")}')
    app.run(
        host='0.0.0.0',
        port=os.environ.get('PORT')
    )
