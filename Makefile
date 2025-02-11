install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

gendiff:
	uv run gendiff

package-install:
	uv pip install dist\hexlet_code-0.1.0-py3-none-any.whl

package-reinstall:
	uv pip install --force-reinstall dist\hexlet_code-0.1.0-py3-none-any.whl

lint:
	uv run ruff check

check: test lint

build:
	uv build

.PHONY: all test clean
