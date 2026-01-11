import random
import time
import requests

URL = "http://127.0.0.1:5000/data"

while True:
    data = {
        "heart_rate": random.randint(60,120),
        "temperature": round(random.uniform(36, 39),2),
        "movement": random.randint(0,2)
    }

    requests.post(URL, json=data)
    print("Sent:", data)
    time.sleep(2)
