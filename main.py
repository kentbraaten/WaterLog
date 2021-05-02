import flask

from flask import request
import json
import io

import logData


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Water Log</h1><p>This site stores data for an small irigation project</p>"



@app.route('/readings/add', methods=['POST'])
def add_reading():

    event = {
        'eventType': request.json.get("eventType"),
        'i2cAddress': request.json.get("i2cAddress"),
        'pin': request.json.get("pin"),
        'reading' : request.json.get("reading"),
        'dateTime': request.json.get("dateTime")
    }

    addedEvent = logData.add_event(event, logData.READINGS_COLLECTION)

    return json.dumps(addedEvent), 201



@app.route('/actions/add', methods=['POST'])
def add_action():

    action = {
        'actionType': request.json.get("actionType"),
        'i2cAddress': request.json.get("i2cAddress"),
        'pin': request.json.get("pin"),
        'dateTime': request.json.get("dateTime")
    }

    addedAction = logData.add_event(action, logData.ACTIONS_COLLECTION)
    return json.dumps(addedAction), 201



@app.route('/systemEvent/add', methods=['POST'])
def add_system_event():

    event = {
        'eventType': request.json.get("eventType"),
        'dateTime': request.json.get("dateTime")
    }

    addedAction = logData.add_event(event, logData.ACTIONS_COLLECTION)
    return json.dumps(addedAction), 201



@app.route('/settings/add', methods=['POST'])
def add_settings():
    addedSettings = logData.add_event(request.json, logData.SETTINGS_COLLECTION)
    return json.dumps(addedSettings), 201

    

@app.route('/settings/current', methods=['GET'])
def return_events_as_json():

    return json.dumps(logData.read_settings())
    


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)