import logging

# Each logger can be configured. The main logger configurations are its:
#     - (a) level
#     - (b) handler(s)

# Note: `basicConfig` is another way to configure root logger
# It creates a handler that comes with a default formatter. That's why when we use `basicConfig`, our messages come in the `WARNING:__main__:msg` format.
# By default, it creates a StreamHandler. But if we pass `filename`, then a FileHandler is created.
# However, I don't like `basicConfig`. Just stick to the more generalised way of configuring a logger (root or not) as shown below.

logger = logging.getLogger("my_logger")

# (a) Level
logger.setLevel(logging.INFO)

# (b) Handlers
file_handler = logging.FileHandler("myapp.log")
stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def main():
    logger.info("Will be logged in myapp.log and console.")


if __name__ == "__main__":
    main()
