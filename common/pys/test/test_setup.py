from .test_authentication import AuthInterceptor
from flask_cors import CORS


class Diplomats(object):
    pass


def fake_setup(app):
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.extensions['diplomats'] = Diplomats()
    AuthInterceptor().init_app(app)
