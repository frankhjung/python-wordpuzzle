#!/usr/bin/env make

ECHO	:= echo
PYTHON	:= python3
SRCS	:= $(wildcard *.py **/*.py)

.DEFAULT_GOAL := help

.PHONY: check clean dist doc help run test

all: check test

help:
	$(ECHO)
	$(ECHO) "Default goal: ${.DEFAULT_GOAL}"
	$(ECHO) "  all:   check cover run test doc dist"
	$(ECHO) "  check: check style and lint code"
	$(ECHO) "  run:   run against test data"
	$(ECHO) "  test:  run unit tests"
	$(ECHO) "  clean: delete all generated files"
	$(ECHO)
	$(ECHO) "Initialise virtual environment (venv) with:"
	$(ECHO)
	$(ECHO) "pip3 install virtualenv; python3 -m virtualenv venv; source venv/bin/activate; pip3 install -r requirements.txt"
	$(ECHO)
	$(ECHO) "Start virtual environment (venv) with:"
	$(ECHO)
	$(ECHO) "source venv/bin/activate"
	$(ECHO)
	$(ECHO) "Deactivate with:"
	$(ECHO)
	$(ECHO) "deactivate"
	$(ECHO)
	$(PYTHON) wordpuzzle.py -h

check:	tags style lint

tags:
	# build python tags
	ctags --recurse -o tags $(SRCS)

style:
	# format code to googles style
	yapf --style google --parallel -i $(SRCS)

lint:
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
	$(RM) -rf cover
	$(RM) -rf .coverage
	$(RM) -rf public
	$(RM) -rf __pycache__ wordpuzzle/__pycache__ tests/__pycache__
	$(RM) -rf .pytest_cache
	$(RM) -rf target
	$(RM) -v MANIFEST
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	$(RM) -v *.pyc *.pyo *.py,cover

#EOF
