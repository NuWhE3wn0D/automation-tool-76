import logging
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configure and return a standard application logger."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

class AutomationLogger:
    """Wrapper class for consistent logging operations."""
    def __init__(self, name: str) -> None:
        self.logger = get_logger(name)

    def info(self, msg: str) -> None:
        """Log info level message."""
        self.logger.info(msg)

    def error(self, msg: str, exc_info: bool = False) -> None:
        """Log error level message."""
        self.logger.error(msg, exc_info=exc_info)