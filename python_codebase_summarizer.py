import argparse
import ast
import os
import fnmatch

class CodeAnalyzer(ast.NodeVisitor):
    """
    A visitor class that uses the AST module to analyze Python source code files.
    Extracts information about functions and classes including their docstrings.
    """
    def __init__(self, include_comments):
        self.found_items = []
        self.indent_level = 0
        self.include_comments = include_comments

    def _add_item(self, item):
        """Adds an item to the list of found items, with indentation based on the current scope level."""
        self.found_items.append("    " * self.indent_level + item)

    def visit_FunctionDef(self, node):
        """Visits a function definition and extracts its name and arguments."""
        function_signature = f"Function: {node.name} - Args: {[arg.arg for arg in node.args.args]}"
        self._add_item(function_signature)
        if self.include_comments and ast.get_docstring(node):
            docstring = "    Docstring:\n    " + "    " * (self.indent_level + 1) + ast.get_docstring(node).replace("\n", "\n    " + "    " * (self.indent_level + 1))
            self._add_item(docstring)
        self.indent_level += 1
        self.generic_visit(node)
        self.indent_level -= 1

    def visit_ClassDef(self, node):
        """Visits a class definition and extracts its name and docstring if present."""
        class_info = f"Class: {node.name}"
        self._add_item(class_info)
        if self.include_comments and ast.get_docstring(node):
            docstring = "    Docstring:\n    " + "    " * (self.indent_level + 1) + ast.get_docstring(node).replace("\n", "\n    " + "    " * (self.indent_level + 1))
            self._add_item(docstring)
        self.indent_level += 1
        self.generic_visit(node)
        self.indent_level -= 1

def normalize_path(path):
    """Normalize a filesystem path for comparison."""
    return os.path.normcase(os.path.abspath(path))

def generate_directory_tree(path, prefix="", exclude_paths=[], exclude_patterns=[]):
    """
    Generates a directory tree for the given path, excluding specified paths.
    """
    
    tree = []
    normalized_path = normalize_path(path)
    if any(normalized_path.startswith(normalize_path(ex)) for ex in exclude_paths):
        return tree
    if prefix:
        tree.append(prefix + os.path.basename(path))
    else:
        tree.append(os.path.basename(path))
    if os.path.isdir(path):
        entries = sorted(os.listdir(path))
        for entry in entries:
            full_entry_path = os.path.join(path, entry)
            if any(fnmatch.fnmatch(full_entry_path, pattern) for pattern in exclude_patterns):
                continue
            if os.path.isdir(full_entry_path):
                tree.extend(generate_directory_tree(full_entry_path, prefix + "    ", exclude_paths, exclude_patterns))
            elif os.path.isfile(full_entry_path):
                if not any(fnmatch.fnmatch(entry, pattern) for pattern in exclude_patterns):
                    tree.append(prefix + "    " + entry)
    return tree

def analyze_code(source_path, include_comments, exclude_paths, exclude_patterns):
    """
    Analyzes the Python code at the given source path, including or excluding specific files or directories.
    """
    
    if os.path.isfile(source_path) and not any(fnmatch.fnmatch(source_path, pattern) for pattern in exclude_patterns):
        files_to_analyze = [source_path]
        directory_tree = []
    elif os.path.isdir(source_path):
        files_to_analyze = []
        normalized_excludes = [normalize_path(p) for p in exclude_paths]
        for root, dirs, files in os.walk(source_path):
            dirs[:] = [d for d in dirs if normalize_path(os.path.join(root, d)) not in normalized_excludes]
            files = [f for f in files if not any(fnmatch.fnmatch(f, pattern) for pattern in exclude_patterns)]
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith(".py") and normalize_path(file_path) not in normalized_excludes:
                    files_to_analyze.append(file_path)
        directory_tree = generate_directory_tree(source_path, exclude_paths=normalized_excludes, exclude_patterns=exclude_patterns)
    else:
        raise Exception(f"The specified path {source_path} is neither a file nor a directory.")

    results = []
    if directory_tree:
        results.append("Directory Tree:\n" + "\n".join(directory_tree) + "\n\n")
    for file in files_to_analyze:
        with open(file, "r", encoding="utf-8") as f:
            node = ast.parse(f.read(), filename=file)
        analyzer = CodeAnalyzer(include_comments)
        analyzer.visit(node)
        results.append(f"Analysis for {file}:\n" + "\n".join(analyzer.found_items))
    return results

def write_to_file(data, output_file):
    """Writes the analyzed data to the specified output file."""
    
    with open(output_file, "w", encoding="utf-8") as file:
        for item in data:
            file.write(f"{item}\n\n")

def main():
    """Main function that parses arguments and runs the code analyzer."""
    
    parser = argparse.ArgumentParser(description="Analyzes Python code and extracts important information such as functions and classes, optionally including docstrings.")
    parser.add_argument("source_path", help="Path to the Python file or directory to be analyzed.")
    parser.add_argument("output_file", help="Path to the text file where the results will be written.")
    parser.add_argument("--comments", action="store_true", help="Includes docstrings from functions and classes.")
    parser.add_argument("--exclude", nargs="*", default=[], help="List of paths to be excluded from analysis.")
    parser.add_argument("--exclude-patterns", nargs="*", default=[], help="List of glob patterns for files to be excluded from analysis (e.g., '*.png', '*.jpg').")

    args = parser.parse_args()

    analyzed_data = analyze_code(args.source_path, args.comments, args.exclude, args.exclude_patterns)
    write_to_file(analyzed_data, args.output_file)

if __name__ == "__main__":
    main()
