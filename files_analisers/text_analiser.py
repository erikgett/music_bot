import requests
import pprint
from settings import hug_token
import pytest
"""
>>> text_analis("good")[0][0]
{'label': 'admiration', 'score': 0.7625299191474915}
"""
API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/bert-base-go-emotion"
headers = {"Authorization": f"Bearer {hug_token}"}
def text_analis(message):
    payload = {"inputs": message}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == '__main__':
    pprint.pprint(text_analis('good'))
    import doctest
    doctest.testmod()
