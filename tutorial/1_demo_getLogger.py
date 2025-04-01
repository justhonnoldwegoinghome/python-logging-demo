import logging

# getLogger returns a logger instance based on the logger's name passed to it as an argument. If no name is passed, it returns the root logger which has a name of `root`.

root_logger = logging.getLogger()

child_1_logger = logging.getLogger("CHILD1")
child_2_logger = logging.getLogger("CHILD2")


def main():
    print(root_logger.name)  # root
    print(root_logger.parent)  # None

    print(child_1_logger.parent.name)  # root
    print(child_2_logger.parent.name)  # root


if __name__ == "__main__":
    main()
