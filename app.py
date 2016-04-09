from flask import render_template
from flask import Flask
import json
import random
import re
import requests
from flask.ext.triangle import Triangle

app = Flask(__name__)
Triangle(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.debug = True
    app.run()