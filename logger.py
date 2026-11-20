import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configure and return a standard application logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_message(logger: logging.Logger, message: str, level: str = "info") -> None:
    """Log a message with a specified severity level."""
    levels = {
        "debug": logger.debug,
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "critical": logger.critical,
    }
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)
