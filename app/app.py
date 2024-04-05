from flask import Flask
from flask import request
from flask_swagger_ui import get_swaggerui_blueprint

import json
import time


app = Flask(__name__)

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to "{SWAGGER_URL}/dist/"
    API_URL,
    config={
        "test_api": "Test application"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/", methods = ["GET","POST"])
def handle_request():
    text = str(request.args.get("input")) # the ?input= a
    character_count = len(text)

    data_set = {"input": text,"timestamp": time.time(), "character_count": character_count}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route("/health", methods = ["GET"])
def health():
    return {"status":"up"}

#@app.route("/ping", methods = ["GET"])
#def ping():
#    return {"ping":"pong"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

