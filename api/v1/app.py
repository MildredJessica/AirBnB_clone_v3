#!/usr/bin/python3
"""API module"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views, __name__)


@app.teardown_appcontext
def teardown_app(exception):
    """Handles what happens when the application context is popped """
    storage.close()

    @app.errorhandler(404)
    def error_handler(code):
        """Handles a 404 error"""
        error = {
            "error": "Not found"
        }
        return jsonify(error, 404)


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port)
