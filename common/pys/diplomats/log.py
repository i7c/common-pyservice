import json_logging
import logging
import os
import sys


initialized = False


def init():
    global initialized

    if not initialized:
        logger = logging.getLogger("system")
        logger.setLevel(os.getenv('LOGLEVEL', 'INFO'))
        logger.addHandler(logging.StreamHandler(sys.stdout))
        logger.debug("common-pys logger initialized")
        initialized = True


class LoggerDiplomat(object):
    def __init__(self, static_data={}):
        json_logging.init_non_web(enable_json=True)
        init()
        logger = logging.getLogger("system")
        self.logger = logger
        self.static_data = static_data

    def log(self, msg, level=logging.INFO, data=None):
        extra = None
        if data:
            extra = {"props": {"data": data}}
        self.logger.log(level=level, msg=msg, extra=extra)

    def debug(self, msg, data={}):
        self.log(msg, level=logging.DEBUG, data={**self.static_data, **data})

    def error(self, msg, data={}):
        self.log(msg, level=logging.ERROR, data={**self.static_data, **data})

    def info(self, msg, data={}):
        self.log(msg, level=logging.INFO, data={**self.static_data, **data})

    def warn(self, msg, data={}):
        self.log(msg, level=logging.WARN, data={**self.static_data, **data})
