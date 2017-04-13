import requests
import json
from flask import Flask,Response,make_response,jsonify,request

class Weather:

    # Constructor
    def __init__(self):
       pass

    def getWeatherForecast():
        city = request.args.get('city');
        if city:
            r = requests.get('https://api.apixu.com/v1/forecast.json?key=c0efcc5afb314c0182a35001171204&q=' + city);
            return Response(json.dumps(r.json()['forecast'], indent=4), 200, mimetype='application/json')
        else :
            return Reponse("INVALID QUERY : Missing the city parameter.", 400)