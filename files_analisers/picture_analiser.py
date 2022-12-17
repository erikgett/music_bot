import requests
import json
from settings import hug_token

API_URL = "https://api-inference.huggingface.co/models/microsoft/beit-base-patch16-224-pt22k-ft22k"
headers = {"Authorization": f"Bearer {hug_token}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

output = query("fire.jpg")
print(output)