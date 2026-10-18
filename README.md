# automation-tool-76

A lightweight, high-performance Python framework designed to streamline repetitive task execution across local and remote environments. This tool minimizes boilerplate code for system administrators and developers looking to orchestrate complex workflows with minimal overhead.

## Features

*   **Task Chaining:** Easily define sequential workflows using YAML configuration files to manage dependencies between processes.
*   **Parallel Execution:** Leverage Python’s `multiprocessing` library to run independent tasks concurrently, significantly reducing overall execution time.
*   **Intelligent Logging:** Automated capture of stdout/stderr streams with configurable log rotation and severity filtering.
*   **Robust Error Handling:** Built-in retry logic and configurable timeout thresholds to ensure stability during unstable network or system conditions.

## Installation

Ensure you have Python 3.8+ installed. You can install the tool directly via pip:

```bash
# Clone the repository
git clone https://github.com/Developer/automation-tool-76.git
cd automation-tool-76

# Install dependencies
pip install -r requirements.txt
```

## Usage

To execute a task defined in your configuration file, use the following command:

```bash
python main.py --config workflows/backup_system.yaml --verbose
```

### Example Config (`workflows/backup_system.yaml`)
```yaml
tasks:
  - name: sync-files
    command: rsync -av /source /destination
    retries: 3
  - name: verify-integrity
    command: ./scripts/check_checksum.sh
    depends_on: sync-files
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.