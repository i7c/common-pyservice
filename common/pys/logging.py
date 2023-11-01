import inspect
import json_logging
import logging
import os
import re
import sys


class LoggerContainer(object):
    initialized = False


def initialize_logger():
    if LoggerContainer.initialized:
        return
    json_logging.init_non_web(enable_json=True)
    # Get root logger
    logger = logging.getLogger()
    logger.setLevel(os.getenv('LOGLEVEL', 'INFO'))
    logger.addHandler(logging.StreamHandler(sys.stdout))
    LoggerContainer.initialized = True
    logger.info("Logger initialized")


def logger(logger_name=None):
    initialize_logger()
    if logger_name:
        return logging.getLogger(logger_name)

    calling_file = inspect.stack()[1].filename
    logger_name = re.sub(r'^.*/', '', calling_file)
    logger_name = re.sub(r'\.[^.]*$', '', logger_name)
    return logging.getLogger(logger_name)
