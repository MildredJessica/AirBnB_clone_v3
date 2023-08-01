#!/usr/bin/python3
"""API views.index module"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slash=False)
def status():
    """Returns a JSON status ok"""
    status = {
        "status": "OK"
    }
    return jsonify(status)
