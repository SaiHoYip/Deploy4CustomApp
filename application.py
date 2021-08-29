from PIL import Image
from flask import Flask, request, Response
import json
application = app = Flask(__name__)
@app.route('/')
def dogPic():
    req = requests.get('https://dog.ceo/api/breeds/image/random')
    imglink = req.json()['message']
    print(imglink)
    return Image.open(requests.get(imglink, stream=True).raw)
