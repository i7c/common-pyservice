from flask import abort, g, request
from functools import wraps
import schema


def coerce(s: schema.Schema):
    def coerce_body_decorator(handler):
        @wraps(handler)
        def coerce_json_body_interceptor(*args, **kwargs):
            try:
                body = request.json
                g.coerced_body = s.validate(body)
            except schema.SchemaError as e:
                print(e)
                abort(400, "Payload does not conform with schema")
            return handler(*args, **kwargs)
        return coerce_json_body_interceptor
    return coerce_body_decorator


def externalize(s: schema.Schema):
    def externalize_body_decorator(handler):
        @wraps(handler)
        def externalize_json_body_interceptor(*args, **kwargs):
            uncoerced_result = handler(*args, **kwargs)
            try:
                return s.validate(uncoerced_result)
            except schema.SchemaError as e:
                print(e)
                abort(500, "Return payload does not conform with schema")
        return externalize_json_body_interceptor
    return externalize_body_decorator
