from flask_cors import CORS


class Diplomats(object):
    pass


def mock_setup(app):
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['CORS_SUPPORTS_CREDENTIALS'] = True
    app.config['CORS_ORIGINS'] = ["http://localhost:5173", "http://localhost"]
    CORS(app)
    app.extensions['diplomats'] = Diplomats()
    app.extensions['config'] = {}
    return app
