setup:
	pip install pipenv
	pipenv install --dev --three

activate:
	pipenv shell -c

test:
	pipenv run -- py.test tests -s -v