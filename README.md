# Word Puzzle Python Solver

This is a Python implementation of the 9-letter word puzzle.

## Quick Start

This project is built using Python 3.9.12.

To get program help call:

```bash
./wordpuzzle.py -h
```

Example call using parameters:

```bash
$ ./wordpuzzle.py -s 8 -l cadevrsoi
codrives
covaried
covaries
discover
divorces
idocrase
varicose
varicosed
```

## Dictionary

To build an English dictionary of valid words, use words from
[wbritish-huge](http://wordlist.sourceforge.net/):

```bash
egrep '^[[:lower:]]+$' /usr/share/dict/british-english-huge > dictionary
```

### Virtual Environment

To initialise the virtual environment, `venv`:

```bash
pip3 install -U virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -Ur requirements.txt
```

To start the virtual environment:

```bash
source venv/bin/activate
```

To end virtual environment session:

```bash
deactivate
```

### Dependent Packages

Install and list packages:

```bash
pip3 install -Ur requirements.txt
pip3 list
pip3 freeze
```

### Format Code

To format code formatter using [Google Python Code
Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md) using
[black](https://github.com/psf/black):

```bash
black *.py library/*.py tests/*.py
```

### Lint Code

Lint source files using both [flake8](https://github.com/pycqa/flake8) and
[Pylint](https://www.pylint.org/):

```bash
flake8 *.py library/*.py tests/*.py
pylint *.py library/*.py tests/*.py
```

### Test application

Test using [PyTest](https://docs.pytest.org/):

```bash
pytest -v --cov-report term-missing --cov=library tests
```

### Run

Run application with:

```bash
python3 wordpuzzle.py -s 7 -l cadevrsoi
```

### Documentation

Get [pydoc](https://docs.python.org/3/library/pydoc.html) using:

```bash
pydoc wordpuzzle
pydoc library.filters
```

## Build and run from Docker

To run using my Docker image first install the default dictionary:

```bash
curl https://raw.githubusercontent.com/dwyl/english-words/master/words.txt -o dictionary
```

Then call the application using GNU make:

```bash
docker run --rm -t -v $PWD:/opt/workspace -u $(id -u):$(id -g) frankhjung/python:latest make exec
```

This will call the `exec` goal, which executes the application using the default
dictionary.

## Tools Used

These tools require Python 3.

- [black](https://github.com/psf/black) - format source files
- [flake8](https://github.com/pycqa/flake8) - checks source files
- [hypothesis](https://hypothesis.readthedocs.io/) - [QuickCheck](https://en.wikipedia.org/wiki/QuickCheck) style testing framework
- [pylint](https://www.pylint.org/) - checks source files
- [pytest](https://docs.pytest.org/) - unit tests
- [venv](https://docs.python.org/library/venv.html) - manage this projects environment

## LICENSE

[GNU GPLv3 LICENSE](./LICENSE)

## References

- [Hypothesis](https://hypothesis.works/)
- [PyTest](https://docs.pytest.org/)
- [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
- [Python Code Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
- [Virtual Environment Tutorial](https://realpython.com/python-virtual-environments-a-primer/)

## Other Implementations

- [Haskell](https://gitlab.com/frankhjung1/haskell-wordpuzzle)
- [Java](https://gitlab.com/frankhjung1/java-wordpuzzle)
- [Kotlin](https://gitlab.com/frankhjung1/kotlin-wordpuzzle)
- [Go](https://gitlab.com/frankhjung1/go-wordpuzzle)
- [Python](https://gitlab.com/frankhjung1/python-wordpuzzle)
