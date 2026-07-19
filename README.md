# Automation Tool 76

Automation Tool 76 is a versatile Python-based utility designed to streamline repetitive tasks within your workflow. From file management to data processing, this tool simplifies complex operations with ease and efficiency.

## Features

- **File Management**: Effortlessly move, copy, and delete files based on specific criteria such as file type or age.
- **Data Processing**: Automate the extraction, transformation, and loading (ETL) of data to and from various formats including CSV, JSON, and XML.
- **Scheduling Tasks**: Integrate cron-like scheduling to run your automation scripts at specified intervals without manual intervention.
- **Log Management**: Generate detailed logs of executed tasks, making troubleshooting and auditing seamless.

## Installation

To get started with Automation Tool 76, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/Developer/automation-tool-76.git
cd automation-tool-76
pip install -r requirements.txt
```

## Basic Usage

Once installed, you can start automating tasks with a simple command. Here’s a basic example of copying all `.txt` files from one directory to another:

```python
from automation_tool import FileManager

file_manager = FileManager(source_directory='source/folder', destination_directory='destination/folder')
file_manager.copy_files(file_extension='.txt')
```

In this example, the `FileManager` class automates the task of copying all text files from the source folder to the destination folder.

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For detailed information on advanced features and usage, please refer to the documentation located in the `docs` directory. Your feedback and contributions are welcome!