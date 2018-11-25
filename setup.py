from setuptools import find_packages
from setuptools import setup

setup(
    packages=find_packages('.', exclude=('tests*', 'testing*')),
    entry_points={
        'console_scripts': [
            'python-todo-check = pre_commit_hook.todo_check:main',
        ],
    },
)

