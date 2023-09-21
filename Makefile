install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=lib test_*.py
	pytest -nbval -v Project1.ipynb

format:	
	black *.py

lint:
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py
	ruff check *.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy
