import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def func1():
    logger.debug("Debug message from func1")
    logger.info("Info message from func1")
    logger.warning("Warning message from func1")
    logger.error("Error message from func1")
    logger.critical("Critical message from func1")
