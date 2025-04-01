"""
- Instantiate one logger per module
- Configure only the root logger in the main module as child loggers will inherit the configuration from the root logger
"""

import logging

formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


file_handler = logging.FileHandler(filename="app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)

root_logger = logging.getLogger()

root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(file_handler)
root_logger.addHandler(stream_handler)


from module1 import func1
from module2 import func2

if __name__ == "__main__":
    root_logger.debug("Debug message from main")
    root_logger.info("Info message from main")
    root_logger.warning("Warning message from main")
    root_logger.error("Error message from main")
    root_logger.critical("Critical message from main")

    func1()
    func2()
