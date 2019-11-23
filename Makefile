#!/usr/bin/env make

.DEFAULT_GOAL := help

.PHONY: check clean dist doc help run test

PYTHON	:= /usr/bin/python3
SRCS	:= $(wildcard *.py **/*.py)

all: check test run

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo "  all:   check cover run test doc dist"
	@echo "  check: check style and lint code"
	@echo "  run:   run against test data"
	@echo "  test:  run unit tests"
	@echo "  clean: delete all generated files"
	@echo
	@echo "Initialise virtual environment (venv) with:"
	@echo
	@echo "pip3 install virtualenv; python3 -m virtualenv venv; source venv/bin/activate; pip3 install -r requirements.txt"
	@echo
	@echo "Start virtual environment (venv) with:"
	@echo
	@echo "source venv/bin/activate"
	@echo
	@echo "Deactivate with:"
	@echo
	@echo "deactivate"
	@echo
	$(PYTHON) wordpuzzle.py -h

check:
	# format code to googles style
	yapf --style google --parallel -i $(SRCS)
	# check with pylint
	pylint $(SRCS)

test:
	pytest -v tests/test*.py

run:
	$(PYTHON) wordpuzzle.py -h
	$(PYTHON) wordpuzzle.py --version
	$(PYTHON) wordpuzzle.py -m c -l adevcrsoi

version:
	$(PYTHON) wordpuzzle.py --version

clean:
	# clean generated artefacts
	$(RM) -rf cover
	$(RM) -rf .coverage
	$(RM) -rf __pycache__ wordpuzzle/__pycache__ tests/__pycache__
	$(RM) -rf public
	$(RM) -rf target
	$(RM) -v MANIFEST
	$(RM) -v *.pyc *.pyo *.py,cover
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover

#EOF
