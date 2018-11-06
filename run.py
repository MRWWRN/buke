#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time, random, hashlib

from flask import Flask, session, request, abort
from apps.admin import admin


app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16M
app.register_blueprint(admin, url_prefix='/admin')

app.secret_key = 'pLWr9 Rj/3yX]asdf3542IJ<><,(*(*&'

@app.before_request
def set_cookies():
    if session.get('login', '') == '':
        try:
            tempname = request.headers.get('User-Agent')[:120] + str(time.time()) + str(random.random())
        except Exception:
            abort(401)
        tempname = hashlib.md5(tempname.encode('utf-8')).hexdigest()
        session['username'] = tempname
        session['login'] = 'false'
    return None

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0')
