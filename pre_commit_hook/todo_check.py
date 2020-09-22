import argparse
import re
import subprocess
import sys
from functools import partial
from pathlib import Path
from typing import List, Tuple


def terminal_run(string_):
    return subprocess.run(string_.split(), stdout=subprocess.PIPE).stdout.decode()


def check_contain_bad_text(text_):
    def check_todo(line_):
        return re.search(r"\btodo\b", line_, re.IGNORECASE)

    def check_pdb(line_):
        return re.search(r"\bimport pdb\b", text_, re.IGNORECASE)

    contain_todo = [
        line_number + 1
        for line_number, line in enumerate(text_.splitlines())
        if check_todo(line)
    ]
    contain_pdb = [
        line_number + 1
        for line_number, line in enumerate(text_.splitlines())
        if check_pdb(line)
    ]
    return contain_todo + contain_pdb


def check_file(base_dir, file_name):
    file_path = base_dir / file_name
    with open(file_path, "r") as f:
        lines_file = (check_contain_bad_text(f.read()), file_path.resolve())
    return lines_file


def set_output(input_stuff: List[Tuple]):
    beginning = "\n\033[91mTodo in Files:"
    files_number = [
        f'\033[36m{" " * 4}{file_path}: line_numbers: {",".join(lines)}'
        for lines, file_path in input_stuff
    ]
    text_to_print = "\n".join([beginning] + files_number)
    return text_to_print


def main(argv=None):
    # get to repo root dir
    base_dir = Path(terminal_run("git rev-parse --show-toplevel").splitlines()[0])
    present_dir = Path("./")

    repo_files = terminal_run(f"git ls-files {base_dir}").splitlines()
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip", nargs="?")
    args = parser.parse_args(argv)

    skip_files = ""
    if args.skip is not None:
        skip_files = [i.strip() for i in args.skip.split(",")]

    files_to_check = [
        str((present_dir / i).resolve()) for i in repo_files if i not in skip_files
    ]
    py_files = [i for i in filter(lambda y: re.search(r".*\.py$", y), files_to_check)]

    check_repo = partial(check_file, base_dir)
    check_files = [py_files(i) for i in check_repo]
    todo_files = [i for i in check_files if len(i[0]) > 0]
    if todo_files:
        sys.stdout.write(set_output(todo_files))
        sys.stdout.write("\n\n\033[0m")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
