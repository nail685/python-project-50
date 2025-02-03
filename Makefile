install:
	uv sync

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

gendiff:
	uv run gendiff

package-install:
	uv -m pip install --user dist/*.whl

package-reinstall:
	uv -m pip install --force-reinstall --user dist/*whl

lint:
	uv run ruff check

selfcheck:
	uv check

check: selfcheck test lint

build: check
	uv build

.PHONY: install test lint selfcheck check build
