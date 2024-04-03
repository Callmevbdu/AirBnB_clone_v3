#!/usr/bin/python3
"""
defines a set of Flask routes for managing Amenity objects within an API.
"""
from flask import jsonify, abort, request
from api.v1.views import app_views, storage
from models.amenity import Amenity


@app_views.route("/amenities", methods=["GET"], strict_slashes=False)
def amenity_get_all():
    """
    Retrieves all Amenity objects from storage and converts them to JSON format
    before returning them.
    """
    am_list = []
    am_obj = storage.all("Amenity")
    for obj in am_obj.values():
        am_list.append(obj.to_json())

    return jsonify(am_list)


@app_views.route("/amenities", methods=["POST"], strict_slashes=False)
def amenity_create():
    """
    Extracts the JSON data from the request, validates it (checks for presence
    of a "name" key), creates a new Amenity object from the data, saves it to
    storage, and returns the newly created amenity object as JSON with a 201
    Created status code.
    """
    am_json = request.get_json(silent=True)
    if am_json is None:
        abort(400, 'Not a JSON')
    if "name" not in am_json:
        abort(400, 'Missing name')

    new_am = Amenity(**am_json)
    new_am.save()
    resp = jsonify(new_am.to_json())
    resp.status_code = 201

    return resp


@app_views.route("/amenities/<amenity_id>",  methods=["GET"],
                 strict_slashes=False)
def amenity_by_id(amenity_id):
    """
    Retrieves a specific Amenity object by its ID from storage, checks if it
    exists, and returns it as JSON. Returns a 404 Not Found status code if the
    amenity is not found.
    """

    fetched_obj = storage.get("Amenity", str(amenity_id))

    if fetched_obj is None:
        abort(404)

    return jsonify(fetched_obj.to_json())


@app_views.route("/amenities/<amenity_id>",  methods=["PUT"],
                 strict_slashes=False)
def amenity_put(amenity_id):
    """
    Extracts the JSON data from the request, validates it (checks if it's a
    JSON object), retrieves the amenity object with the provided ID from
    storage, checks if it exists, iterates over the provided data, updates the
    amenity object's attributes (excluding "id", "created_at", and
    "updated_at"), saves the updated amenity object to storage, and returns the
    updated amenity
    """
    am_json = request.get_json(silent=True)
    if am_json is None:
        abort(400, 'Not a JSON')
    fetched_obj = storage.get("Amenity", str(amenity_id))
    if fetched_obj is None:
        abort(404)
    for key, val in am_json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(fetched_obj, key, val)
    fetched_obj.save()
    return jsonify(fetched_obj.to_json())


@app_views.route("/amenities/<amenity_id>",  methods=["DELETE"],
                 strict_slashes=False)
def amenity_delete_by_id(amenity_id):
    """
    Retrieves a specific Amenity object by its ID from storage, checks if it
    exists, deletes the object from storage, saves the changes, and returns an
    empty JSON dictionary with a 200 OK status code. Returns a 404 Not Found
    status code if the amenity is not found.
    """

    fetched_obj = storage.get("Amenity", str(amenity_id))

    if fetched_obj is None:
        abort(404)

    storage.delete(fetched_obj)
    storage.save()

    return jsonify({})

