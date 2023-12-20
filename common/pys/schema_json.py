from flask import request, g
from functools import wraps
import schema


def coerce(s: schema.Schema):
    def coerce_body_decorator(handler):
        @wraps(handler)
        def coerce_json_body_interceptor(*args, **kwargs):
            body = request.json
            g.coerced_body = s.validate(body)
            return handler(*args, **kwargs)
        return coerce_json_body_interceptor
    return coerce_body_decorator
