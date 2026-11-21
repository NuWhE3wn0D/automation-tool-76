# automation-tool-76

A lightweight, high-performance Python framework designed to streamline repetitive task execution across local and remote environments. This tool abstracts complex CLI operations into a simple, programmatic interface to save development time.

### Features

*   **Task Orchestration:** Execute sequences of system commands with built-in dependency management and error handling.
*   **Parallel Execution:** Leverage a multi-threaded engine to run independent tasks concurrently, significantly reducing total runtime.
*   **Modular Plugins:** Extend functionality using custom Python modules or integrate with existing environment variables seamlessly.
*   **Detailed Logging:** Comprehensive console and file-based output tracking to simplify debugging and auditing of automation workflows.

### Installation

Requires Python 3.8+ and `pip`.

```bash
# Clone the repository
git clone https://github.com/Developer/automation-tool-76.git
cd automation-tool-76

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

Define your automation logic in a Python script or use the CLI runner to execute a task file.

**As a CLI tool:**
```bash
python main.py run --file tasks.yaml
```

**As a library:**
```python
from automation_tool import TaskRunner

runner = TaskRunner()
runner.add_task("cleanup", "rm -rf ./temp/*")
runner.execute()
```

### Configuration
Update the `config.json` file in the root directory to define global execution parameters, timeout thresholds, and directory paths.

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.