import logging
import sys
from typing import Optional


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configure and return a standard application logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


class AppLogger:
    """Logger wrapper for consistent automation-tool-76 logging output."""

    def __init__(self, name: str) -> None:
        self.logger = setup_logger(name)

    def info(self, message: str) -> None:
        """Log informational messages."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        """Log error messages with optional exception details."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Log warning messages."""
        self.logger.warning(message)