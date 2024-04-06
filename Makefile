build:
	docker-compose build

up:
	docker-compose up -d app

down:
	docker-compose down --remove-orphans

docker-implode:
	docker-compose down --remove-orphans --rmi all

logs:
	docker-compose logs app | tail -100

bash: up
	docker-compose exec app bash

test: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /src/utilities/tests/unit /src/utilities/tests/integration /src/utilities/tests/e2e

unit-tests:
	docker-compose run --rm --no-deps --entrypoint=pytest app /src/utilities/tests/unit

integration-tests: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /src/utilities/tests/integration

e2e-tests: up
	docker-compose run --rm --no-deps --entrypoint=pytest app /src/utilities/tests/e2e

rest: up
	docker-compose up rest-app

black:
	black -l 86 $$(find * -name '*.py')

clean: clean-build clean-pyc clean-test
	echo "Clean complete."

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

.PHONY: help Makefile

