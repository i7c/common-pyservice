from .authentication import AuthInterceptor
from .cache import no_caching
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
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    app.config['CORS_ORIGINS'] = ["http://localhost:5173",
                                  "http://localhost",
                                  "https://ui.decentrafly.org"]
    CORS(app)
    no_caching(app)
    app.extensions['diplomats'] = Diplomats()
    app.extensions['config'] = {}
    AuthInterceptor().init_app(app)
    return app
