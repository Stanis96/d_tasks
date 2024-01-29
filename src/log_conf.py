import logging
import sys


class LogFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno < self.level


def set_up_logger():
    MIN_LEVEL = logging.DEBUG
    stdout_hdlr = logging.StreamHandler(sys.stdout)
    stderr_hdlr = logging.StreamHandler(sys.stderr)
    log_filter = LogFilter(logging.WARNING)
    stdout_hdlr.addFilter(log_filter)
    stdout_hdlr.setLevel(MIN_LEVEL)
    stderr_hdlr.setLevel(max(MIN_LEVEL, logging.WARNING))
    rootLogger = logging.getLogger()
    rootLogger.addHandler(stdout_hdlr)
    rootLogger.addHandler(stderr_hdlr)
    formatter = logging.Formatter(
        "%(asctime)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
    )
    stdout_hdlr.setFormatter(formatter)
    stderr_hdlr.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.setLevel(
        logging.DEBUG,
    )
    return logger


logger = set_up_logger()
