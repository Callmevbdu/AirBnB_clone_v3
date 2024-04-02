#!/usr/bin/python3
"""
Create Flask App.
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import specific views from api.v1.views
from api.v1.views.index import *
