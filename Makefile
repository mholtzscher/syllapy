setup:
	poetry install
	poetry run pre-commit install

test:
	poetry run pytest --cov=syllapy -q tests/

ci-test:
	poetry run pytest tests/ --cov=syllapy --cov-report html
	poetry run codecov

lint:
	poetry run pylint syllapy

mypy:
	poetry run mypy syllapy

format:
	poetry run black syllapy tests