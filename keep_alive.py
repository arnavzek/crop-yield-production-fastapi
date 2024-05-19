import requests
import time
import threading

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def keep_alive():
    print("Keeping Alive")
    threading.Timer(5.0, keep_alive).start()
    url = "https://crop-yield-production-fastapi.onrender.com/yields/?state=rajasthan&area=200"  # Replace with your desired URL
    send_request(url)
