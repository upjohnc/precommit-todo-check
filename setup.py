from setuptools import setup

setup(
    name='pre_commit_todo_check',
    version='0.0.0',
    entry_points={
        'console_scripts': [
            'todo_check = pre_commit.todo_check:main',
        ],
    },
)
