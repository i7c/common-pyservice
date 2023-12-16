from flask import current_app


class Null(object):
    pass


def dipl():
    return current_app.extensions['diplomats']


def cfg():
    return current_app.extensions['config']
