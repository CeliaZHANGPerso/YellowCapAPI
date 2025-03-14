import pickle
from utils import transform_input 

def predict(input):
    model = pickle.load(open("yellowcab/model/forest_model.pkl", 'rb'))
    transformed_input = transform_input(input)
    prediction = model.predict(transformed_input)
    return prediction
