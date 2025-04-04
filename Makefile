setup-python-env:
	@echo "Setting up Python environment..."
	cp .env.dist .env
	python3 -m venv ./venv/

install:
	@echo "Installing dependencies..."
	source ./venv/bin/activate && \
	python -m pip install -r requirements.txt

freeze:
	@echo "Freezing packages..."
	source ./venv/bin/activate && \
	pip freeze > requirements.txt


docker:
	@echo "Building Docker image..."
	docker-compose up --build

run-locally:
	@echo "Running the application..."
	source ./venv/bin/activate && \
	python run.py

tests:
	@echo "Running tests..."
	source ./venv/bin/activate && \
	coverage run -m unittest && \
	coverage html && \
	coverage xml

lint:
	@echo "Linting the code..."
	source ./venv/bin/activate && \
	python -m pylint --reports=True ./app ./test

pre-commit:
	@echo "Running pre-commit hooks..."
	pre-commit run
