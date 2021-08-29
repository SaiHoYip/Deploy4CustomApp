from flask import Flask, request, Response
import json
application = app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello world'
