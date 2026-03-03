import argparse
import ast
from .renamer import RenameTransformer
from .formatter import simple_format
import difflib

def process_file(path: str, dry_run: bool=False):
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    tree = ast.parse(code)
    tree = RenameTransformer().visit(tree)
    ast.fix_missing_locations(tree)
    new_code = ast.unparse(tree)
    new_code = simple_format(new_code)
    if dry_run:
        diff = difflib.unified_diff(code.splitlines(), new_code.splitlines(), fromfile='before', tofile='after', lineterm='')
        print('\n'.join(diff))
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_code)

def main():
    parser = argparse.ArgumentParser(description='Clean Python code')
    parser.add_argument('file', help='Python file to clean')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without writing')
    args = parser.parse_args()
    process_file(args.file, args.dry_run)
if __name__ == '__main__':
    main()