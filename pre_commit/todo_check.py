import re
import subprocess
import sys
from pathlib import Path

base_dir = Path(__file__).parent.parent.parent.resolve()


def check_contain_todo(text_):
    return re.search(r'\btodo\b', text_, re.IGNORECASE)


def check_file(file_name):
    with open(base_dir / file_name, 'r') as f:
        return check_contain_todo(f.read())


skip_files = ('nifi/scripts/score_validation.py', 'stream-generator/stream_generator/qpp/submission_logs.py')
files_to_check = [i.decode() for i in subprocess.run(['git', 'ls-files'], stdout=subprocess.PIPE).stdout.splitlines() if i.decode() not in skip_files]
py_files = [i for i in filter(lambda y: re.search('.*\.py$', y), files_to_check)]


def main():
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
