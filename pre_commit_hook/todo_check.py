import argparse
import re
import subprocess
import sys
from functools import partial
from pathlib import Path


def terminal_run(string_):
    return subprocess.run(string_.split(), stdout=subprocess.PIPE).stdout.decode()


def check_contain_bad_text(text_):
    contain_todo = re.search(r'\btodo\b', text_, re.IGNORECASE)
    contain_pdb = re.search(r'\bimport pdb\b', text_, re.IGNORECASE)
    return any((contain_pdb, contain_todo))


def check_contain_todo(text_):
    contain_todo = re.search(r'\btodo\b', text_, re.IGNORECASE)
    return contain_todo


def check_file(base_dir, file_name):
    with open(base_dir / file_name, 'r') as f:
        return check_contain_todo(f.read())


def main(argv=None):
    # get to repo root dir
    base_dir = Path(terminal_run('git rev-parse --show-toplevel').splitlines()[0])
    present_dir = Path('./')

    repo_files = terminal_run(f'git ls-files {base_dir}').splitlines()
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to skip')
    parser.add_argument('--skip', nargs='?')
    args = parser.parse_args(argv)

    skip_files = ''
    if args.skip is not None:
        skip_files = [i.strip() for i in args.skip.split(',')]

    files_to_check = [str((present_dir / i).resolve()) for i in repo_files if i not in skip_files]
    py_files = [i for i in filter(lambda y: re.search(r'.*\.py$', y), files_to_check)]

    check_repo = partial(check_file, base_dir)
    todo_files = tuple(filter(check_repo, py_files))
    if todo_files:
        sys.stdout.write("\n\033[91mTodo in Files:\n")
        for i in todo_files:
            sys.stdout.write(f'{" " * 4}{i}\n')
        sys.stdout.write('\n\n\033[0m')
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
