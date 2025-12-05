#!/usr/bin/env make

.PHONY: all check clean help run tags test version

.DEFAULT_GOAL := default

CTAGS	:= $(shell which ctags)
PYTHON	:= $(shell which python3)
SRCS	:= $(wildcard *.py **/*.py)
COVERAGE	:= 90

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
	@echo "Initialise environment with:"
	@echo
	@echo "  uv sync"
	@echo
	@echo "Run commands with:"
	@echo
	@echo "  uv run <command>"
	@echo
	@uv run python wordpuzzle.py -h

check:	tags style lint

tags:
ifdef CTAGS
	# build ctags for vim
	ctags --recurse -o tags $(SRCS)
endif

style:
	uv run ruff format
	uv run sort-requirements requirements.txt 2>/dev/null || true

lint:
	uv run ruff check \
		--output-format grouped \
		--fix $(SRCS)

test:
	uv run pytest --verbose --cov-fail-under=$(COVERAGE) library/ tests/

doc:
	uv run pytest \
		--junitxml=public/pytest_report.xml \
      		--html=public/pytest_report.html \
		--self-contained-html \
      		--cov \
      		--cov-report=xml \
		--cov-report=html:public/coverage \
		--cov-fail-under=$(COVERAGE)
	uv run pdoc library !tests -o public

run:
	uv run python wordpuzzle.py -s 7 -l cadevrsoi

version:
	uv run python wordpuzzle.py --version

clean:
	# clean generated artefacts
	-$(RM) -rf cover
	-$(RM) -rf .coverage
	-$(RM) -rf __pycache__ **/__pycache__
	-$(RM) -rf .pytest_cache
	-$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	-$(RM) -v *.pyc *.pyo *.py,cover

#EOF
