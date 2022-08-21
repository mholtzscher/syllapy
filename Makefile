setup:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics

mypy:
	mypy syllapy

format:
	black .

format-check:
	black . --check