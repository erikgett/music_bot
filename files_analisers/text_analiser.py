import requests
import pprint
from settings import hug_token

API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/bert-base-go-emotion"
headers = {"Authorization": f"Bearer {hug_token}"}


def query(message):
    payload = {"inputs": message}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


if __name__ == '__main__':
    pprint.pprint(query('good'))
