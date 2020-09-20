setup:
	pip install --upgrade pip
	pip install -r requirements.txt
	pre-commit install

test:
	pytest --cov=syllapy -q tests/

lint:
	flake8

mypy:
	mypy syllapy

format:
	black syllapy tests setup.py