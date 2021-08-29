import requests
from PIL import Image
from flask import Flask, request, Response
import json
application = app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
  
req = requests.get('https://dog.ceo/api/breeds/image/random')
imglink = req.json()['message']
print(imglink)
Image.open(requests.get(imglink, stream=True).raw)
