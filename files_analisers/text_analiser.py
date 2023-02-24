import pprint

import requests

from settings import hug_token

API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/bert-base-go-emotion"
headers = {"Authorization": f"Bearer {hug_token}"}


def text_analis(message):
    payload = {"inputs": message}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def test_text_analis():
    assert text_analis('good')[0][0] == {'label': 'admiration', 'score': 0.7525299191474915}


if __name__ == '__main__':
    pprint.pprint(text_analis('good'))
