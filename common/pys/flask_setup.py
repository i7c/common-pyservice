from .cache import no_caching
from flask_cors import CORS


class Diplomats(object):
    pass


def setup(app):
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    app.config['CORS_ORIGINS'] = ["http://localhost:5173", "http://localhost"]
    CORS(app)
    no_caching(app)
    app.extensions['diplomats'] = Diplomats()
    app.extensions['config'] = {}
    return app
