import argparse
import re
import subprocess
import sys
from pathlib import Path


def terminal_run(string_):
    return subprocess.run(string_.split(), stdout=subprocess.PIPE).stdout.decode()


base_dir = Path(terminal_run('git rev-parse --show-toplevel').splitlines()[0])


def check_contain_todo(text_):
    return re.search(r'\btodo\b', text_, re.IGNORECASE)


def check_file(file_name):
    with open(base_dir / file_name, 'r') as f:
        return check_contain_todo(f.read())


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to skip')
    args = parser.parse_args(argv)

    skip_files = args.filenames#('nifi/scripts/score_validation.py', 'stream-generator/stream_generator/qpp/submission_logs.py')
    files_to_check = [i for i in terminal_run('git ls-files').splitlines() if i not in skip_files]
    print(skip_files, files_to_check)
    py_files = [i for i in filter(lambda y: re.search('.*\.py$', y), files_to_check)]

    todo_files = tuple(filter(check_file, py_files))
    if todo_files:
        sys.stdout.write("\n\033[91mTodo in Files:\n")
        for i in todo_files:
            sys.stdout.write(f'{" " * 4}{i}\n')
        sys.stdout.write('\n\n\033[0m')
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
