import requests
from PIL import Image
application = app = Flask(__name__)
req = requests.get('https://dog.ceo/api/breeds/image/random')
imglink = req.json()['message']
print(imglink)
Image.open(requests.get(imglink, stream=True).raw)
