from flask import Flask, render_template, request
import requests
import json

def get_iss_data():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    return json.loads(response.text)

def is_ISS_overhead(iss_lat, iss_lon, user_lat, user_lon):
    # Here, we assume if the ISS is within +/- 5 degrees of the user's location, it's overhead.
    # You could modify this based on your needs.
    return abs(iss_lat - user_lat) <= 5 and abs(iss_lon - user_lon) <= 5

def get_user_location():
    ip = request.remote_addr

    if ip == '127.0.0.1:5000' or 'localhost' or '127.0.0.1' or 'localhost:5000':
        ip = '41.95.255.34'

    response = requests.get(f"http://ip-api.com/json/{ip}")
    return json.loads(response.text)

def get_static_map_url(lat, lon):

    access_token = 'pk.eyJ1IjoiZHlsYW5uZ3V5ZW4yMzMxIiwiYSI6ImNsa3d4dHVsczAyemszc282Y3Z0cmNkMTAifQ.ZEakIyBGFJDAcowB9oi6WA'
    return f"https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/pin-s+FF0000({lon},{lat})/{lon},{lat},2,0/600x300?access_token={access_token}"