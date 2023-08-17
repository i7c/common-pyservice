from .authentication import AuthInterceptor
from flask_cors import CORS
import os
import sys


class Diplomats(object):
    pass


def fail(message):
    print(message)
    sys.exit(2)


def setup(app):
    if not os.getenv('JWKS_ENDPOINT'):
        fail("You must set env var JWKS_ENDPOINT")
    if not os.getenv('JWT_AUDIENCE'):
        fail("You must set env var JWT_AUDIENCE")
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.extensions['diplomats'] = Diplomats()
    AuthInterceptor().init_app(app)
