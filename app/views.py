from . import app
import sys
import os
from flask import Flask, render_template, url_for, jsonify, request
import pandas as pd
import numpy as np

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html')

@app.route("/vicini-di-casa")
def vicini_di_casa():

    return render_template("vicini di casa.html")

@app.route("/grammatica.html")
def grammatica():

    return render_template("grammatica.html")

@app.route("/domanda-di-sport")
def domanda_di_sport():

    return render_template("domanda di sport.html")