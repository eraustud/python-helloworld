from flask import Flask
app = Flask(__name__)

import json

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response_dict = {
        "result": "OK - healthy"
    }
    response = app.response_class(
        response = json.dumps(response_dict),
        status=200,
        mimetype="application/json"
    )
    return response

@app.route("/metrics")
def metrics():
    data_dict = {
        "UserCount": "140",
        "UserCountActive": "23"
    }
    response_dict = {
        "data": data_dict
    }
    response = app.response_class(
        response = json.dumps(response_dict),
        status=200,
        mimetype="application/json"
    )
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0")
