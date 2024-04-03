#!/usr/bin/python3
"""
Create Flask App.
"""

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from os import getenv
from api.v1.views import app_views

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Register blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """
    teardown function
    """
    storage.close()


@app.errorhandler(404)
def handle_404(exception):
    """
    returns '404' error
    """
    data = {
        "error": "Not found"
    }

    response = jsonify(data)
    response.status_code = 404

    return (response)


# Run the Flask server
if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
