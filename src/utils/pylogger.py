import logging


def get_pylogger(name=__name__):
    """pylogger for logging the in the framework."""

    logger = logging.getLogger(name)

    # this ensures all logging levels get marked with the rank zero decorator
    # otherwise logs would get multiplied for each GPU process in multi-GPU setup
    # logging_levels = ("debug", "info", "warning", "error", "exception", "fatal", "critical")
    logger.setLevel(logging.DEBUG)
    return logger
