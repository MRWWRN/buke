#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from flask import Blueprint

admin = Blueprint('admin', __name__, static_folder='stc', template_folder='templates')

from . import views

