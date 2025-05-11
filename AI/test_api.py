import requests


url = 'http://127.0.0.1:5000/predict'

# ✅ Replace these with actual feature values expected by your model
data = {
    'features': [0.5, 1.2, 3.1, 4.7, 2.0, 3.3, 0.8, 1.5]  # 8 values!
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
