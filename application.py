from PIL import Image
from flask import Flask, request, Response
import json
application = app = Flask(__name__)
@app.route('/')
    req = requests.get('https://catfact.ninja/fact')
    print(req.status_code)
    print(req.json())

    if req.status_code == 200:
        return print(f"Your fact of the day is: {req.json()['fact']}")
    else: 
        return print("nope")
