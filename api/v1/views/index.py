#!/usr/bin/python3
"""API views.index module"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', strict_slash=False)
def status():
    """Returns a JSON status ok"""
    status = {
        "status": "OK"
    }
    return jsonify(status)


@app_views.route('/stat', strict_slash=False)
def count():
    """Retrieves the number of each objects by type"""
    models_avail = {
        "User": "users",
        "Amenity": "amenities", "city": "cities",
        "Place": "places", "Review": "reviews",
        "State": "states",
    }

    count = {}
    for cls in models_avail.keys():
        count[models_avail[cls]] = storage.count(cls)
    return jsonify(count)
