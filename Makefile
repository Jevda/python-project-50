# Makefile для проекта Gendiff

install:
	uv pip install '.[dev]'

lint:
	uv run ruff check .

test:
	uv run pytest

test-coverage:
	# ИЗМЕНЕНО: Указываем новую папку для измерения покрытия
	uv run pytest --cov=gendiff --cov-report xml

check:
	make lint
	make test

build:
	uv build

clean:
	rm -rf dist/
	rm -rf .pytest_cache/
	rm -f coverage.xml
	rm -rf *.egg-info/
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: install lint test test-coverage check build clean