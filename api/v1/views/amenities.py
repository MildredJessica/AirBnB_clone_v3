#!usr/bin/python3
"""View for Amenity objects that handles all default RESTFul API actions"""

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import jsonify, abort, make_response, request


@app_views.route('/amenities', methods=['GET'])
@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenityy(amenity_id):
    """Retrieves  list of all Amenities or an Amenity object"""
    if amenity_id is None:
        all_amenities = [state.to_dict() for state
                         in storage.all(Amenity).values()]
        return jsonify(all_amenities)
    sto = storage.get(Amenity, amenity_id)
    if sto is None:
        abort(404)
    return jsonify(sto.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id=None):
    """"Deletes a amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    """"Creates an Amenity"""
    try:
        req = request.get_json()
    except Exception:
        req = None
    if req is None:
        return "Not a JSON", 400
    if 'name' not in req.keys():
        return 'Missing name', 400
    amenity = Amenity(**req)

    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id=None):
    """"Updates a amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    try:
        req = request.get_json()
    except Exception:
        req = None
    if req is None:
        return "Not a JSON", 400
    for key in ("id", "created_at", "updated_at", "state_id"):
        req.pop(key, None)
    for key, value in req.items():
        setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
