# automation-tool-76

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

`automation-tool-76` is a lightweight, extensible Python utility designed to streamline repetitive local workflows and file management tasks. It eliminates manual friction by batch-processing routine operations through a clean, configuration-driven interface.

## Features

- **Batch File Transformations:** Quickly rename, move, or convert directory structures using custom YAML rules.
- **Scheduled Execution:** Run background tasks at specified intervals without relying on heavy system cron jobs.
- **Actionable Logging:** Outputs colorized, structured logs to the console while maintaining a detailed audit trail in `automation.log`.
- **Plugin Architecture:** Easily write custom Python scripts to extend core capabilities for specialized local environments.

## Installation

Ensure you have Python 3.8 or higher installed on your system. 

```bash
# Clone the repository
git clone https://github.com/Developer/automation-tool-76.git
cd automation-tool-76

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Create a `config.yaml` file in the root directory to define your tasks:
```yaml
tasks:
  - name: "organize-downloads"
    source: "~/Downloads"
    destination: "~/Documents/Archive"
    file_types: [".pdf", ".docx"]
    action: "move"
```

2. Run the tool to execute your automation sequence:
```bash
python main.py --config config.yaml
```

To run in continuous monitoring mode, append the `--watch` flag:
```bash
python main.py --config config.yaml --watch
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.