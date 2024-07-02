from flask import Flask, request, jsonify
import utility

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : utility.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bedrooms = int(request.form['bedrooms'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bedrooms,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

if __name__ == "__main__":
    print("starting python flask server")
    app.run()