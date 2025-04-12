from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("store_size_model.joblib")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        features = data['features']
        prediction = model.predict([features])
        return jsonify({'prediction': prediction.tolist()})
    else:
        return "Send a POST request with JSON input."

@app.route('/')
def home():
    return "Welcome to the ML model API! Use /predict with POST method."


if __name__ == '__main__':
    app.run(debug=True)