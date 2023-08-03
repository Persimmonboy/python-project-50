install:
	poetry install

test:
	poetry run pytest

run:
	poetry run gendiff --help

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

patch:
	poetry install
	poetry build
	poetry publish --dry-run --username ' ' --password ' '
	python -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

.PHONY: install test lint selfcheck check build