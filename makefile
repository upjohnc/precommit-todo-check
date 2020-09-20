SHELL := bash
.ONESHELL:
.RECIPEPREFIX = >

root_dir = ./pre_commit_hook

test:
> poetry run pytest -v

isort:
> poetry run isort . .isort.cfg
