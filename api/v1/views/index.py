#!/usr/bin/python3
"""
Create Flask App
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def api_status():
    """Returns a JSON response indicating the API status."""
    data = {
        "status": "OK"
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp
