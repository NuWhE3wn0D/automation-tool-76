import logging
import sys
from pathlib import Path

def get_logger(name: str, log_file: str = "app.log", level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        
    return logger

def rotate_logs(log_path: str, max_files: int = 5) -> None:
    path = Path(log_path)
    if not path.exists():
        return
    
    for i in range(max_files - 1, 0, -1):
        src = Path(f"{log_path}.{i}")
        dst = Path(f"{log_path}.{i+1}")
        if src.exists():
            src.rename(dst)
            
    path.rename(f"{log_path}.1")