import logging
from logging.handlers import RotatingFileHandler

LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.INFO
LOG_FILE = 'app.log'

handler = RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=2)
handler.setFormatter(logging.Formatter(LOG_FORMAT))

logger = logging.getLogger('AutomationTool76')
logger.setLevel(LOG_LEVEL)
logger.addHandler(handler)