#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from run import app
from flask import render_template

@app.route('/')
def index():
    return '''<h1>布克</h1>'''

@app.route('/login')
def login():
    return render_template('login.html')
