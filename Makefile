install:
	uv install

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

gendiff:
	uv run gendiff

lint:
	uv run flake8

selfcheck:
	uv check

check: selfcheck test lint

build: check
	uv build

.PHONY: install test lint selfcheck check build
