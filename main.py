import flask
from flask import request
import json

import logData


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Water Log</h1><p>This site stores data for an small irigation project</p>"


@app.route('/events/add', methods=['POST'])
def add_event():
    event = {
        'eventType': request.json.get("eventType"),
        'i2cAddress': request.json.get("i2cAddress"),
        'pin': request.json.get("pin"),
        'reading' : request.json.get("reading"),
        'dateTime': request.json.get("dateTime")
    }
    addedEvent = logData.add_event(event)
    return json.dumps(addedEvent), 201


@app.route('/events/all', methods=['GET'])
def return_events_as_json():
    return json.dumps(logData.read_events())
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)