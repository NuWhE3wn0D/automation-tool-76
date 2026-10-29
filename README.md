# automation-tool-76

A lightweight, high-performance Python framework designed to streamline repetitive task execution across local and remote environments. It provides a robust engine for scheduling, chaining workflows, and logging execution metrics with minimal overhead.

## Features

*   **Task Chaining:** Easily define sequential dependencies between multiple scripts to create complex automation pipelines.
*   **Dynamic Scheduling:** Built-in cron-style scheduler with support for sub-second precision and flexible job intervals.
*   **Asynchronous Execution:** Utilizes `asyncio` to run parallel tasks, significantly reducing total runtime for I/O-bound operations.
*   **Integrated Monitoring:** Real-time logging of task success, failure, and execution latency, with exportable JSON output for audit trails.

## Installation

Ensure you have Python 3.9+ installed. You can install the tool directly via pip:

```bash
# Clone the repository
git clone https://github.com/Developer/automation-tool-76.git
cd automation-tool-76

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

Create a `tasks.yaml` file to define your routine, then execute the tool using the following command:

```bash
python main.py --config tasks.yaml --verbose
```

**Example task configuration:**

```yaml
tasks:
  - name: cleanup-temp
    command: "rm -rf /tmp/app/*"
    interval: "3600" # Runs every hour
  - name: sync-logs
    command: "python scripts/sync.py --remote"
    depends_on: cleanup-temp
```

For advanced scripting, you can import the engine as a library:

```python
from automation_tool import Engine

engine = Engine(config="tasks.yaml")
engine.run_all()
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.