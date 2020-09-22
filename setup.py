from setuptools import find_packages, setup

setup(
    packages=find_packages(".", exclude=("tests*", "testing*")),
    entry_points={"console_scripts": ["python-todo-check = todo_check:main"]},
)
