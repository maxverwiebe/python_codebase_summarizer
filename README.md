# Python Codebase Summarizer

Python Code Analyzer is a tool designed to analyze Python code within a single file or recursively through directories. It extracts important information like function and class definitions, including their docstrings, and provides an overview of the directory structure.
**It's made to feed your AI Chatbot with information about your codebase!**

## Features

- Analyze single Python files or entire directories.
- Extract function signatures and class definitions.
- Optionally include docstrings in the analysis output.
- Exclude specific files, directories, or match patterns to ignore during analysis.
- Generate a directory tree showing the structure of analyzed directories.

## Requirements

- Python 3.x
- No external libraries required beyond the Python Standard Library.

## Usage

### Command-Line Arguments

- `source_path`: Path to the Python file or directory to be analyzed.
- `output_file`: Path to the text file where the results will be written.
- `--comments`: Include docstrings from functions and classes in the output.
- `--exclude`: Provide a space-separated list of paths to exclude from analysis.
- `--exclude-patterns`: Provide a space-separated list of glob patterns for files to be excluded from analysis (e.g., '*.png', '*.jpg').

### Example Commands

```bash
# Analyze a single Python file and include docstrings in the output.
python python_codebase_summarizer.py my_script.py output.txt --comments

# Analyze a directory and exclude specific sub-directories or files.
python python_codebase_summarizer.py my_project/ results.txt --exclude my_project/tests/ my_project/deprecated.py

# Analyze a directory and exclude files matching patterns.
python python_codebase_summarizer.py my_project/ results.txt --exclude-patterns '*.png' '*.jpg'
```

## Output

The output text file will contain:

* A directory tree (if a directory is analyzed).
* Extracted information for each Python file analyzed:
  * Functions with their names and arguments.
  * Classes with their names.
  * Optionally, docstrings for functions and classes.
 
## Contributing

Contributions to the Python Code Analyzer are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more information.
