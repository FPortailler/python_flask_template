setup-python-env:
	@echo "Setting up Python environment..."
	cp .env.dist .env
	python3 -m venv ./venv/

install-dev:
	@echo "Installing dependencies..."
	source ./venv/bin/activate && \
	python -m pip install -r requirements/dev.txt

install-qa:
	@echo "Installing dependencies..."
	source ./venv/bin/activate && \
	python -m pip install -r requirements/qa.txt

install-prod:
	@echo "Installing dependencies..."
	source ./venv/bin/activate && \
	python -m pip install -r requirements/prod.txt

freeze:
	@echo "Freezing packages..."
	source ./venv/bin/activate && \
	pip freeze > requirements.txt


run:
	@echo "Building Docker image..."
	docker-compose up --build

run-locally:
	@echo "Running the application..."
	source ./venv/bin/activate && \
	python run.py

tests:
	@echo "Running tests..."
	source ./venv/bin/activate && \
	coverage run --rcfile=./.coveragerc -m unittest  && \
	coverage html && \
	coverage xml

lint:
	@echo "Linting the code..."
	source ./venv/bin/activate && \
	python -m pylint --reports=True ./app ./test \

format:
	@echo "Running black..."
	source ./venv/bin/activate && \
	black --config black.config.toml ./app ./test

pre-commit:
	@echo "Running pre-commit hooks..."
	pre-commit run
