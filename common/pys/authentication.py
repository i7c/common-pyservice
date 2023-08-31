from flask import abort, request, g
from jwt import PyJWKClient, decode
import os
import re


class AuthInterceptor(object):
    auth_header_payload = re.compile("Bearer[\s]+")

    def __init__(self):
        self.jwkclient = PyJWKClient(os.getenv('JWKS_ENDPOINT'))

    def init_app(self, app):
        app.extensions['unsecure_routes'] = []

        def interceptor():
            if request.path in app.extensions['unsecure_routes']:
                return
            try:
                if request.method == "OPTIONS":
                    return
                auth_header = request.headers.get('authorization')
                cookie = request.cookies.get("dcfsession")
                if not auth_header and cookie:
                    auth_header = cookie

                if not auth_header or auth_header.isspace():
                    abort(401)
                if not auth_header.startswith('Bearer'):
                    abort(401)
                payload = AuthInterceptor.auth_header_payload.sub("", auth_header)
                signing_key = self.jwkclient.get_signing_key_from_jwt(payload)
                token = decode(
                    payload,
                    signing_key.key,
                    algorithms=["RS256"],
                    audience=os.getenv('JWT_AUDIENCE')
                )
                g.auth_identity = token
            except Exception as e:
                print("Authentication failed hard: {}".format(e))
                abort(401)

        app.before_request(interceptor)


def unsecure_route(app, route):
    app.extensions['unsecure_routes'].append(route)
