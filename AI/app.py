from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("store_size_model.joblib")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        data = request.get_json()
        features = data['features']

        if len(features) != 8:
            return jsonify({'error': f'Expected 8 features, got {len(features)}'}), 400

        prediction = model.predict([features])
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/')
def home():
    return "Welcome to the ML model API! Use /predict with POST method."

if __name__ == '__main__':
    app.run(debug=True)