import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


def func2():
    logger.debug("Debug message from func2")
    logger.info("Info message from func2")
    logger.warning("Warning message from func2")
    logger.error("Error message from func2")
    logger.critical("Critical message from func2")
