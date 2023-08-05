from flask import Flask, render_template, request
import requests
import json

def get_apod():
    api_key = "loxUlDve1ZSbxn4sDDIiokWW7ewAQdJ3fjfTHchm"
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")
    data = response.json()
    return data