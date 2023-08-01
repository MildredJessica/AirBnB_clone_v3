#!/usr/bin/python3
"""API module"""

from flask import Flask, Blueprint
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views, __name__)


@app.teardown_appcontext
def teardown_app(exception):
    """Handles what happens when the application context is popped """
    storage.close()


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
