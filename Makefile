#!/usr/bin/env make

.PHONY: all check clean help run tags test version

.DEFAULT_GOAL := default

PIP	:= pip3
PYTHON	:= python3
SRCS	:= $(wildcard *.py **/*.py)

default: check test

all:	default run

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

check:	tags style lint

tags:
	# build python tags
	ctags --recurse -o tags $(SRCS)

style:
	# sort imports
	isort $(SRCS)
	# format code to googles style
	black -q $(SRCS)

lint:
	# check with flake8
	flake8 $(SRCS)
	# check with pylint
	pylint $(SRCS)

test:
	pytest -v --cov-report term-missing --cov=lib tests

run:
	$(PYTHON) wordpuzzle.py -s 7 -l cadevrsoi

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
