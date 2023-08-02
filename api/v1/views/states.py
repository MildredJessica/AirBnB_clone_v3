#!usr/bin/python3
"""View for State objects that handles all default RESTFul API actions"""

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, make_response, request


@app_views.route('/states', methods=['GET'], strict_slash=False)
def all_states():
    """Gets all the states """
    all_states = storage.all(State).values()
    state_list = []

    for state in all_states:
        state_list.append(state.to_dict())

    return jsonify(state_list), 200


@app_views.route('/states/<state_id>', methods=['GET'], strict_slash=False)
def get_states(state_id=None):
    """Retrieves a State object"""
    if state_id is None:
        abort(404)
    state = storage.get('State', state_id)  # get state object
    if state is None:
        abort(404)
<<<<<<< HEAD

    return jsonify(state.to_json)
=======
    return jsonify(state.to_json)


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slash=False)
def delete_states(state_id=None):
    """"Deletes a state object"""
    if state_id is None:
        abort(404)
    state = storage.get('State', state_id)  # get state object
    if state is None:
        abort(404)
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slash=False)
def post_states(state_id=None):
    """"Creates a state"""
    if request.get_json():
        kwargs = request.get_json()
    else:
        return "Not a JSON", 400
    if kwargs:
        if 'name' not in kwargs.keys():
            return 'Missing name', 400
    try:
        state = State(**kwargs)
        state.save()
    except TypeError:
        return "Not a JSON", 400
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states', methods=['PUT'], strict_slash=False)
def update_states(state_id=None):
    """"Updates a state object"""
    if request.get_json():
        kwargs = request.get_json()
    else:
        return "Not a JSON", 400
    if kwargs:
        if 'name' not in kwargs.keys():
            return 'Missing name', 400
    try:
        state = storage.get(state, state_id)
        if state is None:
            abort(404)
        for key in ("id", "created_at", "updated_at"):
            kwargs.pop(key, None)
            for value in kwargs.items():
                setattr(state, key, value)
        state.save()
    except (Exception):
        return "Not a JSON", 400
    return jsonify(state.to_dict()), 200
>>>>>>> master
