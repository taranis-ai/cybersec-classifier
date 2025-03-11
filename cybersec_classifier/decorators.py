from flask import request
from functools import wraps

from cybersec_classifier.config import Config
from cybersec_classifier.log import Logger


def api_key_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not Config.API_KEY:
            return fn(*args, **kwargs)

        error = ({"error": "not authorized"}, 401)
        auth_header = request.headers.get("Authorization", None)

        if not auth_header or not auth_header.startswith("Bearer"):
            logger.warning("Missing Authorization Bearer")
            return error

        api_key = auth_header.replace("Bearer ", "")

        if Config.API_KEY != api_key:
            logger.warning("Incorrect api key")
            return error

        # allow
        return fn(*args, **kwargs)

    return wrapper
