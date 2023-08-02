#!usr/bin/python3
"""View for City objects that handles all default RESTFul API actions"""

from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from flask import jsonify, abort, make_response, request


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def all_cities_in_state(state_id):
    """Retrieves the list of all City objects of a State"""

    state = storage.get(State, state_id)
    if state_id is None:
        abort(404)
    city_list = []
    for city in state.city:
        city_list.append(city.to_dict())

    return jsonify(city_list)


@app_views.route('cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """Retrieves a City object"""
    city = storage.get('City', city_id)  # get City object
    if city is None:
        abort(404)
    return jsonify(city.to_json)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slash=False)
def delete_aCity(city_id):
    """"Deletes a city object"""
    city = storage.get('City', city_id)  # get city object
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_aCity(state_id):
    """"Creates a city"""
    try:
        req = request.get_json()
    except Exception:
        req = None
    if req is None:
        return "Not a JSON", 400
    if 'name' not in req.keys():
        return 'Missing name', 400
    city = City(**req)
    city.state_id = state_id
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slash=False)
def update_aCity(city_id):
    """"Updates a state object"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    try:
        req = request.get_json()
    except Exception:
        req = None
    if req is None:
        return "Not a JSON", 400
    for key in ("id", "created_at", "updated_at", "state_id"):
        req.pop(key, None)
    for key, value in req.items():
        setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200
