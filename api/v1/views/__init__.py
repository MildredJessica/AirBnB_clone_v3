#!usr/bin/python3
"""Blueprint Initialization"""

from flask import Blueprint
from api.v1.views import *
from api.v1.views import (
    states, cities, amenities, users, places, places_reviews)


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
