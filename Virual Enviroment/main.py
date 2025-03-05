import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/1"  # Sample API
    data = fetch_data(url)
    if data:
        print("Fetched Data:", data)
