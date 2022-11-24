import json
import requests
from settings import hug_token

API_URL = "https://api-inference.huggingface.co/models/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
headers = {"Authorization": f"Bearer {hug_token}"}


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


if __name__ == '__main__':
    import pprint
    pprint.pprint(query(r'01. Felix Jaehn & Ray Dalton - Call It Love.mp3'))

