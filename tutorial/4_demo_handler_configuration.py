import logging

# Each handler can be configured. The main handler configurations are its:
#     - (a) level (notice that `level` exists on handlers and loggers. If a logger logs something above its level, it still has to 'clear' its handler's level.)
#     - (b) formatter

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(filename="myapp.log")
file_handler.setLevel(logging.WARNING)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def main():
    logger.info("Will be logged by stream handler but not file handler.")


if __name__ == "__main__":
    main()
