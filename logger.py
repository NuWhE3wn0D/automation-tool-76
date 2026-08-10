import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_size=10*1024*1024, backup_count=5):
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()  
logger.info('Logger initialized')