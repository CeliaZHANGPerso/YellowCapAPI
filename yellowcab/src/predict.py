import pickle
from utils import transform_input 

def predict_duration(input, path_model="yellowcab/model/forest_model.pkl") -> int:
    model = pickle.load(open(path_model, 'rb'))
    transformed_input = transform_input(input)
    prediction = model.predict(transformed_input)
    return prediction
