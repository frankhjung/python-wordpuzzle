#!/usr/bin/env make

PIP	:= pip3
PYTHON	:= python3
SRCS	:= $(wildcard *.py **/*.py)

.DEFAULT_GOAL := help

.PHONY: all check clean help run setup tags test version

all: check test

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
	@echo "pip3 install -U virtualenv; python3 -m virtualenv venv; source venv/bin/activate; pip3 install -U -r requirements.txt"
	@echo
	@echo "Start virtual environment (venv) with:"
	@echo
	@echo "source venv/bin/activate"
	@echo
	@echo "Deactivate with:"
	@echo
	@echo "deactivate"
	@echo
	@$(PYTHON) wordpuzzle.py -h

setup:
	$(PIP) install -U virtualenv
	$(PYTHON) -m virtualenv venv
	source venv/bin/activate
	$(PIP) install -U -r requirements.txt

check:	tags style lint

tags:
	# build python tags
	ctags --recurse -o tags $(SRCS)

style:
	# sort imports
	isort $(SRCS)
	# format code to googles style
	yapf --style google --parallel -i $(SRCS)

lint:
	# check with flake8
	flake8 $(SRCS)
	# check with pylint
	pylint $(SRCS)

test:
	pytest -v tests/test*.py

run:
	$(PYTHON) wordpuzzle.py -m c -l adevcrsoi

version:
	$(PYTHON) wordpuzzle.py --version

clean:
	# clean generated artefacts
	-$(RM) -rf cover
	-$(RM) -rf .coverage
	-$(RM) -rf public
	-$(RM) -rf __pycache__ **/__pycache__
	-$(RM) -rf .pytest_cache
	-$(RM) -rf target
	-$(RM) -v MANIFEST
	-$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	-$(RM) -v *.pyc *.pyo *.py,cover

#EOF
