import logging
import sys
from typing import Optional

class AutomationLogger:
    def __init__(self, name: str = "automation-tool-76", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        return self.logger

def setup_default_logger(name: str = "automation-tool-76") -> logging.Logger:
    return AutomationLogger(name).get_logger()