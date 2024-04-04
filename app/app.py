from flask import Flask
from flask import request
import json
import time

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def handle_request():
    text = str(request.args.get('input')) # the ?input= a
    character_count = len(text)

    data_set = {'input': text,'timestamp': time.time(), 'character_count': character_count}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/ping', methods = ['GET'])
def ping():
    return {"ping":"pong"}

#@app.route('/health', methods = ['GET'])
#def health():
#    return {"status":"up"}
