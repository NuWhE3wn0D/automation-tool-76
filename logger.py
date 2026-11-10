import logging
import sys
from pathlib import Path
from typing import Optional


class AutomationLogger:
    """Custom logger setup for automation workflows."""

    def __init__(
        self,
        name: str = "automation",
        log_dir: Optional[Path] = None,
        level: int = logging.INFO,
    ) -> None:
        """Initialize the logger with stdout and optional file handler."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.handlers.clear()

        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        if log_dir:
            log_dir.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(
                log_dir / f"{name}.log", encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        """Return the configured logging.Logger instance."""
        return self.logger


def setup_logger(
    name: str = "automation",
    log_dir: Optional[Path] = None,
    level: int = logging.INFO,
) -> logging.Logger:
    """Helper function to instantiate and retrieve a configured logger."""
    wrapper = AutomationLogger(name=name, log_dir=log_dir, level=level)
    return wrapper.get_logger()
