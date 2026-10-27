.PHONY: install test lint format

install:
	python -m pip install -e ".[dev]"
	pre-commit install

test:
	pytest --cov=physproj --cov-report=term-missing

lint:
	ruff check .
	ruff format --check .

format:
	ruff check --fix .
	ruff format .
