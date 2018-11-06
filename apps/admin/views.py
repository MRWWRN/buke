#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from flask import render_template

from . import admin


@admin.route('/')
def login():
    return render_template('admin/index.html')
