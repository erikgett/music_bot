import requests
import json
from settings import hug_token
import pytest


API_URL = "https://api-inference.huggingface.co/models/microsoft/beit-base-patch16-224-pt22k-ft22k"
headers = {"Authorization": f"Bearer {hug_token}"}

def pick_query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

if __name__ == '__main__':
    output = pick_query("fire.jpg")
    print(output)