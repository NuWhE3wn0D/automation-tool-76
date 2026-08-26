# automation-tool-76

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

`automation-tool-76` is a lightweight, extensible Python utility designed to streamline repetitive local workflows and data processing tasks. It replaces fragile shell scripts with a robust, configuration-driven engine that executes routine operations reliably.

## Features

- **YAML-Based Workflows**: Define complex sequences of file operations, API calls, and system commands using clean, human-readable YAML configuration files.
- **Concurrent Execution**: Speed up batch processing operations utilizing an integrated thread pool for parallel task execution.
- **Built-in Error Recovery**: Configure automatic retries, exponential backoff, and fallback routines for unstable network or file I/O operations.
- **Detailed Audit Logging**: Output structured JSON logs to track execution metrics, success rates, and failure points across all runs.

## Installation

Ensure you have Python 3.9 or higher installed on your system. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/automation-tool-76.git
cd automation-tool-76
pip install -r requirements.txt
```

To install the tool globally in editable mode, run:

```bash
pip install -e .
```

## Usage

1. Create a workflow configuration file named `workflow.yaml`:

```yaml
name: daily-cleanup
tasks:
  - name: archive-logs
    action: move_files
    params:
      source_dir: "./logs"
      dest_dir: "./archive"
      extension: ".log"
  - name: ping-webhook
    action: http_request
    params:
      url: "https://discord.com/api/webhooks/example"
      method: "POST"
      payload: {"content": "Log archive completed successfully."}
```

2. Execute the automation tool by passing your configuration file:

```bash
autotool76 run --config workflow.yaml
```

For dry-run testing without executing side effects, append the `--dry-run` flag:

```bash
autotool76 run --config workflow.yaml --dry-run
```

## License

This project is licensed under the terms of the [MIT License](LICENSE).