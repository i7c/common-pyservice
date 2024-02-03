import json_logging
import logging
import os
import sys


class LoggerDiplomat(object):
    def __init__(self):
        json_logging.init_non_web(enable_json=True)
        logger = logging.getLogger("system")
        logger.setLevel(os.getenv('LOGLEVEL', 'INFO'))
        logger.addHandler(logging.StreamHandler(sys.stdout))
        logger.debug("common-pys logger initialized")
        self.logger = logger

    def log(self, msg, level=logging.INFO, data=None):
        extra = None
        if data:
            extra = {"props": {"data": data}}
        self.logger.log(level=level, msg=msg, extra=extra)

    def debug(self, msg, data=None):
        self.log(msg, level=logging.DEBUG, data=data)

    def error(self, msg, data=None):
        self.log(msg, level=logging.ERROR, data=data)

    def info(self, msg, data=None):
        self.log(msg, level=logging.INFO, data=data)

    def warn(self, msg, data=None):
        self.log(msg, level=logging.WARN, data=data)
