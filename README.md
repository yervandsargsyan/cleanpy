# cleanpy

Simple Python code cleaner.

## Install

```bash
pip install -e .
```

## Use

Run cleanpy on a Python file (overwrite the file), or see changes without writing using dry-run:

```bash
# Overwrite the file
python -m cleanpy.cli example.py

# Show changes/diffs only (dry-run)
python -m cleanpy.cli example.py --dry-run