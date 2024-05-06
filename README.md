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

### Example
```txt
Analysis for _test.py:
Class: CodeAnalyzer
    Docstring:
        A visitor class that uses the AST module to analyze Python source code files.
        Extracts information about functions and classes including their docstrings.
    Function: __init__ - Args: ['self', 'include_comments']
    Function: _add_item - Args: ['self', 'item']
        Docstring:
            Adds an item to the list of found items, with indentation based on the current scope level.
    Function: visit_FunctionDef - Args: ['self', 'node']
        Docstring:
            Visits a function definition and extracts its name and arguments.
    Function: visit_ClassDef - Args: ['self', 'node']
        Docstring:
            Visits a class definition and extracts its name and docstring if present.
Function: normalize_path - Args: ['path']
    Docstring:
        Normalize a filesystem path for comparison.
Function: generate_directory_tree - Args: ['path', 'prefix', 'exclude_paths', 'exclude_patterns']
    Docstring:
        Generates a directory tree for the given path, excluding specified paths.
Function: analyze_code - Args: ['source_path', 'include_comments', 'exclude_paths', 'exclude_patterns']
    Docstring:
        Analyzes the Python code at the given source path, including or excluding specific files or directories.
Function: write_to_file - Args: ['data', 'output_file']
    Docstring:
        Writes the analyzed data to the specified output file.
Function: main - Args: []
    Docstring:
        Main function that parses arguments and runs the code analyzer.

```
 
## Contributing

Contributions to the Python Code Analyzer are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more information.
