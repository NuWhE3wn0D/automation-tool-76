import logging
import sys
from typing import Any, Optional

class Logger:
    def __init__(self, name: str = "automation", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        if not isinstance(message, str) or not message.strip():
            self.logger.warning("Invalid info message: empty or non-string")
            return
        try:
            self.logger.info(message)
        except Exception as e:
            print(f"Failed to log info: {e}")

    def error(self, message: str, exception: Optional[Exception] = None) -> None:
        if not isinstance(message, str) or not message.strip():
            message = "An error occurred with invalid message"
        try:
            if exception:
                self.logger.error(f"{message} - {type(exception).__name__}: {str(exception)}")
            else:
                self.logger.error(message)
        except Exception as e:
            print(f"Failed to log error: {e}")
            try:
                with open("error_fallback.log", "a") as f:
                    f.write(f"{message}\n")
            except:
                pass

    def handle_edge_case(self, value: Any, operation: str) -> bool:
        if value is None:
            self.error("None value provided for operation", ValueError("None input"))
            return False
        if operation == "divide":
            if not isinstance(value, (int, float)) or value == 0:
                self.error("Invalid divisor", ValueError("Zero or non-numeric"))
                return False
        elif operation == "parse":
            if not isinstance(value, str):
                self.error("Invalid parse input", TypeError("Expected string"))
                return False
            if not value:
                self.error("Empty string for parse")
                return False
        return True

    def log_exception(self, exc: Exception) -> None:
        if exc is None:
            self.error("No exception to log")
            return
        try:
            self.logger.exception(f"Exception occurred: {str(exc)}")
        except Exception as e:
            print(f"Logging exception failed: {e}")