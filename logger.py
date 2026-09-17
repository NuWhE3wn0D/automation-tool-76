import logging
import sys
from typing import Optional

class AutomationLogger:
    """Standardized logging utility for automation-tool-76."""

    def __init__(self, name: str, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log an informational message."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[Exception] = None) -> None:
        """Log an error message with optional exception details."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Log a warning message."""
        self.logger.warning(message)

def get_logger(name: str) -> AutomationLogger:
    """Factory function for creating logger instances."""
    return AutomationLogger(name)