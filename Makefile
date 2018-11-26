setup:
	poetry install
	poetry run pre-commit install

test:
	poetry run pytest --cov=syllapy -q tests/

lint:
	poetry run pylint syllapy

mypy:
	poetry run mypy syllapy

format:
	poetry run black syllapy tests