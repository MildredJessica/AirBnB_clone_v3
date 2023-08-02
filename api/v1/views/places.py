#!usr/bin/python3
"""View for Places objects that handles all default RESTFul API actions"""

from api.v1.views import app_views
from models import storage
from models.place import Place
from flask import jsonify, abort, make_response, request


@app_views.route('/places', methods=['GET'])
@app_views.route('/places/<place_id>', methods=['GET'])
def get_placey(place_id):
    """Retrieves  list of all places or a place object"""
    if place_id is None:
        all_places = [
            place.to_dict() for place in storage.all(Place).values()]
        return jsonify(all_places)
    sto = storage.get(Place, all_places)
    if sto is None:
        abort(404)
    return jsonify(sto.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id=None):
    """"Deletes a place object"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    return jsonify({}), 200


@app_views.route('/place', methods=['POST'])
def create_place():
    """"Creates an place"""
    try:
        req = request.get_json()
    except Exception:
        req = None
    if req is None:
        return "Not a JSON", 400
    if 'name' not in req.keys():
        return 'Missing name', 400
    places = Place(**req)

    return jsonify(places.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id=None):
    """"Updates a place object"""
    place = storage.get(Place, place_id)
    try:
        req = request.get_json()
    except Exception:
        req = None
    if req is None:
        return "Not a JSON", 400
    for key in ("id", "created_at", "updated_at", "state_id"):
        req.pop(key, None)
    for key, value in req.items():
        setattr(Place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200
