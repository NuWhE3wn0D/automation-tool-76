[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# automation-tool-76

`automation-tool-76` is a lightweight Python engine designed to streamline repetitive filesystem operations and API orchestration tasks. It provides developers with a unified interface to watch directories, execute concurrent HTTP requests, and schedule recurring local scripts with minimal overhead.

## Features

* **Smart Directory Watcher:** Monitor specific paths for file creations or modifications and trigger customized data processing pipelines.
* **Concurrent API Batching:** Dispatch bulk asynchronous HTTP requests with built-in rate-limiting, exponential backoff, and failure recovery.
* **Declarative Task Scheduling:** Define and execute cron-like workflows directly inside your Python scripts using an intuitive decorator syntax.

## Installation

Install the package via pip:

```bash
pip install automation-tool-76
```

## Quick Start

The following example demonstrates how to set up a scheduled directory cleanup and compress files automatically.

```python
from automation_tool_76 import TaskRunner, FileSystem

# Initialize the automation engine
runner = TaskRunner()
fs = FileSystem()

@runner.task(interval="1h")
def archive_old_reports():
    # Find and compress CSV files older than 7 days
    target_files = fs.find_files("./data", pattern="*.csv", age_days=7)
    if target_files:
        fs.zip_files(target_files, destination="./archives/monthly_report.zip")
        print(f"Archived {len(target_files)} reports successfully.")

if __name__ == "__main__":
    runner.start()
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

---
Developed by Developer.