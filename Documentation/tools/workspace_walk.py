"""Walk workspace files without descending into local references or Git data."""
import os
from pathlib import Path


def workspace_files(root):
    root = Path(root)
    for folder, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d != '.git' and
                   not (Path(folder) == root and d == '.reference-cache')]
        for name in files:
            yield Path(folder) / name
