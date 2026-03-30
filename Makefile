#!/usr/bin/env make

.PHONY: all check clean help run tags test version

.DEFAULT_GOAL := default

CTAGS	:= $(shell which ctags)
PYTHON	:= $(shell which python3)
SRCS	:= $(wildcard *.py **/*.py)
COVERAGE	:= 90

default: check test ## Default goal: check style and lint code, then run unit tests

all:	default run ## Run all checks, then run against test data

help:
	@echo ""
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
	@echo ""
	@echo "To initialize and install dependencies managed by uv:"
	@echo ""
	@echo "  uv sync"
	@echo ""
	@echo "To run commands in the virtual environment:"
	@echo ""
	@echo "  uv run <command>"
	@echo ""
	@uv run python wordpuzzle.py -h

check:	tags style lint ## Check code style and lint

tags: ## Generate ctags for vim
ifdef CTAGS
	# build ctags for vim
	ctags --recurse -o tags $(SRCS)
endif

style: ## Check code style
	uv run ruff format
	uv run sort-requirements requirements.txt 2>/dev/null || true

lint: ## Check code style and lint
	uv run ruff check \
		--output-format grouped \
		--fix $(SRCS)

test: ## Run unit tests
	uv run pytest --verbose --cov-fail-under=$(COVERAGE) library/ tests/

doc: ## Create documentation
	uv run pytest \
		--junitxml=public/pytest_report.xml \
      		--html=public/pytest_report.html \
		--self-contained-html \
      		--cov \
      		--cov-report=xml \
		--cov-report=html:public/coverage \
		--cov-fail-under=$(COVERAGE)
	uv run pdoc library !tests -o public

run: ## Run against test data
	uv run python wordpuzzle.py -s 7 -l cadevrsoi

version: ## Show version
	uv run python wordpuzzle.py --version

update: ## Update dependencies
	uv pip list --outdated
	uv sync --upgrade

clean: ## Delete all generated files
	# clean generated artefacts
	-$(RM) -rf cover
	-$(RM) -rf .coverage
	-$(RM) -rf __pycache__ **/__pycache__
	-$(RM) -rf .pytest_cache
	-$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	-$(RM) -v *.pyc *.pyo *.py,cover
