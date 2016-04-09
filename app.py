from flask import render_template
from flask import Flask
from flask import jsonify
import json
import random
import re
import requests
from flask.ext.triangle import Triangle
import csv

app = Flask(__name__)
Triangle(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/data')
def data():
    with open("static/data/augmented_volunteers.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        results = []
        for row in reader:
            results.append(row)
        final_results = {
            "status": "success",
            "data": results
        }
        return jsonify(**final_results)


if __name__ == '__main__':
    app.debug = True
    app.run()