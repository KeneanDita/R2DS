from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("store_size_model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract and reshape the features
        features = data['features']  # Should be a list of 8 values
        prediction = model.predict([features])[0]

        return jsonify({'predicted_size': prediction})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)