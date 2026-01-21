run:
	python src/main.py
test:
	pytest
setup:
	pip install -r requirements.txt
	pre-commit install
check:
	black .
	isort .
	flake8 .
	pytest
