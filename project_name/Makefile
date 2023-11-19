.PHONY: setup setup-dev check syntax fmt test kernel start-lab

TEST_TARGET=$(if $(COVERAGE),test-coverage,test)

MODULES:=project_name tests

setup-dev: setup
	pip install -e .["dev"]

check: check-types check-syntax $(TEST_TARGET)

check-types:
	mypy --config-file mypy.ini $(addprefix -p ,$(MODULES))

check-syntax:
	flake8 $(MODULES)
	pylint --rcfile .pylintrc --ignore-patterns='.*flycheck.*' $(MODULES)

fmt:
	black $(MODULES)

test:
	python -m unittest discover tests

test-coverage:
	coverage run -m unittest discover tests
	coverage report -m

kernel: setup
	python -m ipykernel install --user --name python-yototec --display-name "Python (Yototec)"

start-lab:
	jupyter lab
