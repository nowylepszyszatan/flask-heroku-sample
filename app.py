import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def coTamSlychacZielonyLudku():
  return "Hello all"

@app.route('/goodbye')
def index_bye():
  return "good bye"

