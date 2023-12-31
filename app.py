from flask import Flask, render_template, request
from iss_tracker import *
from apod import *
from datetime import date
import requests
import json
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/iss_tracker')
def iss_tracker():
    user_location = get_user_location()
    iss_data = get_iss_data()
    iss_latitude = float(iss_data['iss_position']['latitude'])
    iss_longitude = float(iss_data['iss_position']['longitude'])
    
    if is_ISS_overhead(iss_latitude, iss_longitude, user_location['lat'], user_location['lon']):
        message = "The ISS is currently overhead!"
    else:
        message = "The ISS is not overhead at the moment."

    static_map_url = get_static_map_url(iss_latitude, iss_longitude)

    return render_template('iss_tracker.html', message=message, static_map_url=static_map_url, iss_latitude=iss_latitude, iss_longitude=iss_longitude)

@app.route('/climate_change')
def climate_change():
    return render_template('climate_change.html')

@app.route('/apod')
def apod():
    currDate = date.today()

    apod_data = get_apod()
    return render_template('apod.html', apod_data=apod_data, currDate=currDate)


if __name__ == '__main__':
    app.run(debug=True)


