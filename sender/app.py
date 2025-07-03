import requests
import time

receiver_url = "http://receiver:5001/message"

data = {"from": "Sender", "text": "Hello from Sender!"}

time.sleep(3)  # Wait to ensure receiver is ready

print("📤 Sending message to receiver...")
res = requests.post(receiver_url, json=data)

print("📬 Response from receiver:")
print(res.json())
