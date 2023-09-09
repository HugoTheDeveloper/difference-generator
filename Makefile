install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest tests

test-vv:
	poetry run pytest tests -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test-coverage-console:
	poetry run pytest --cov=gendiff

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build