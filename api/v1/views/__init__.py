#!/usr/bin/python3
"""
Create Flask App.
"""


app_views = Blueprint('/api/v1', __name__, url_prefix='/api/v1')


from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
