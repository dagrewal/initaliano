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

@app.route("/about")
def about():

    return render_template("about.html")