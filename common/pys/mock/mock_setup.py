from .mock_authentication import MockAuthInterceptor
from flask_cors import CORS


class Diplomats(object):
    pass


def mock_setup(app):
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.extensions['diplomats'] = Diplomats()
    MockAuthInterceptor().init_app(app)
