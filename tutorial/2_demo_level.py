import logging

# Each logger can be configured.

root_logger = logging.getLogger()
logging.basicConfig(level=logging.WARNING)


def main():
    root_logger.info("Will not be logged.")
    root_logger.warning("Will be logged.")


if __name__ == "__main__":
    main()
