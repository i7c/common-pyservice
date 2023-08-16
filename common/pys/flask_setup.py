from .authentication import AuthInterceptor
from flask_cors import CORS


def setup(app):
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    AuthInterceptor().init_app(app)
