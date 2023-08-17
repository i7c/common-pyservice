from flask import current_app


def dipl():
    return current_app.extensions['diplomats']
