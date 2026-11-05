import os
from pathlib import Path
from typing import Dict, Any

BASE_DIR = Path(__file__).resolve().parent

DEFAULT_CONFIG: Dict[str, Any] = {
    "log_level": "INFO",
    "timeout": 30,
    "retry_attempts": 3,
    "output_dir": BASE_DIR / "output"
}

def load_config(env_vars: Dict[str, str] = None) -> Dict[str, Any]:
    config = DEFAULT_CONFIG.copy()
    env = env_vars or os.environ
    
    if "APP_LOG_LEVEL" in env:
        config["log_level"] = env["APP_LOG_LEVEL"]
    if "APP_TIMEOUT" in env:
        config["timeout"] = int(env["APP_TIMEOUT"])
        
    config["output_dir"].mkdir(parents=True, exist_ok=True)
    return config

settings = load_config()