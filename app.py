from flask import Flask
from flask import current_app, flash, jsonify, make_response, redirect, request, url_for, render_template

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import os
import json
import requests
import io

import pyrebase

API_KEY = 'ffb5aa052bb34a36b29b0cedc4b9eeec'
API_SECRET = 'BZ2o0ZgeXtBzHxQlfoiO2gd9DjadFFq3iX05KzZktcHKm742g5gHKt8F'
API_URL = 'https://api.receptiviti.com/v1/score'

# create firestone db
cred = credentials.Certificate("./keys.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# create flask app
app = Flask(__name__)

"""
Functions needed:
- get_payload (Receptiviti class)
- receptiviti_api (Receptiviti class)
- populate (route) - fill all profiles
- analyze_image (route)
- get_word_cloud (route)
- analyze_text_response (route)
"""

# default route
@app.route("/")
def populate():
    documents = db.collection(u'users').where(u'profiles.default.isComplete', u'==', True).stream()
    name = []
    for doc in documents:
        doc_id = doc.id
        name = doc.to_dict()['profiles']['default']['fullName']
        string = 'Name: ' + name + '|| ID: ' + doc_id
        names.append(string)
    return str(names)

# Receptiviti class
class Receptiviti():
    def get_payload(self, text):
        if len(text)<1:
            print("Error: 'text' should not be empty")
            return {}
        if isinstance(text, str):
            return ({
                "content": text
            }, API_URL)
        if isinstance(text, list):
            return ([{
                "content": content
            } for content in text], API_URL + '/bulk')

    def receptiviti_api(self, text):
        payload, url = self.get_payload(text)
        results = []
        if len(payload)>0:
            response = requests.post(url, data=json.dumps(payload), auth=(API_KEY, API_SECRET), headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                results = response.json()
        return results

# run app if this .py is run
if __name__ == "__main__":
    app.run()