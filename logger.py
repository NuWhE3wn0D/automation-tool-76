import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, level=logging.INFO):
    logger = logging.getLogger(name)
    handler = RotatingFileHandler(log_file, maxBytes=1e6, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger('my_logger', 'app.log')
    logger.info('Logger is set up and running')