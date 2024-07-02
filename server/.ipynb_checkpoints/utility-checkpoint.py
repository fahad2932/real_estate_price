import pickle
import numpy as np

__location = None
__data_columns = None
__model = None

def get_estimate(location,sqft,bedrooms,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zero(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bedrooms
    if loc_index >= 0 :
        x[loc_index] = 1

    return __model.predict([x])

def get_locations_name():
    return __locations

def load_data():
    global __data_columns
    global __locations
    global __model 
    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open("./artifacts/prediction.pickle",'rb') as f:
       __model = pickle.load(f)
        
if __name__ == "__main__":
    load-data()
    print(get_location_name())

