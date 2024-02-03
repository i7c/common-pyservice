from flask import abort, g
from functools import wraps


def requires_group(group: str):
    def auth_checker_decorator(handler):
        @wraps(handler)
        def auth_checker_cognito_group_interceptor(*args, **kwargs):
            token = g.auth_identity
            if not token or group not in token.get("cognito:groups", []):
                abort(401, "Unauthorized")
            return handler(*args, **kwargs)
        return auth_checker_cognito_group_interceptor
    return auth_checker_decorator
