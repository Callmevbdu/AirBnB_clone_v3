#!/usr/bin/python3
"""
Create Flask App
"""

from flask import jsonify
from api.v1.views import app_views  # Import the blueprint


@app_views.route('/status')
def api_status():
    """Returns a JSON response indicating the API status."""
    return jsonify({'status': 'OK'})
