import logging


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def log_error(logger, message):
    logger.error(message)


def log_warning(logger, message):
    logger.warning(message)


def log_info(logger, message):
    logger.info(message)


def log_debug(logger, message):
    logger.debug(message)