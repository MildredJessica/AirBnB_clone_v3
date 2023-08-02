#!usr/bin/python3
"""View for Users objects that handles all default RESTFul API actions"""

from api.v1.views import app_views
from models import storage
from models.user import User
from flask import jsonify, abort, make_response, request


@app_views.route('/users', methods=['GET'])
@app_views.route('/users/<user_id>', methods=['GET'])
def get_amenityy(user_id):
    """Retrieves  list of all Users or a user object"""
    if user_id is None:
        all_users = [
            user.to_dict() for user in storage.all(User).values()]
        return jsonify(all_users)
    sto = storage.get(User, all_users)
    if sto is None:
        abort(404)
    return jsonify(sto.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id=None):
    """"Deletes a users object"""
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'])
def create_users():
    """"Creates an users"""
    try:
        req = request.get_json()
    except Exception:
        req = None
    if req is None:
        return "Not a JSON", 400
    if 'name' not in req.keys():
        return 'Missing name', 400
    users = User(**req)

    return jsonify(users.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def update_amenity(user_id=None):
    """"Updates a user object"""
    user = storage.get(User, user_id)
    try:
        req = request.get_json()
    except Exception:
        req = None
    if req is None:
        return "Not a JSON", 400
    for key in ("id", "created_at", "updated_at", "state_id"):
        req.pop(key, None)
    for key, value in req.items():
        setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
